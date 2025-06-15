const pc = new RTCPeerConnection();
const remoteVideo = document.getElementById("remoteVideo");

navigator.mediaDevices.getUserMedia({ video: true, audio: false })
    .then(stream => {
        stream.getTracks().forEach(track => pc.addTrack(track, stream));
    })
    .catch(error => {
        console.error("Error accessing media devices:", error);
    });

pc.onicecandidate = event => {
    if (event.candidate) {
        // Handle ICE candidates if needed
    }
};

pc.ontrack = event => {
    remoteVideo.srcObject = event.streams[0];
};

async function createOffer() {
    try {
        const offer = await pc.createOffer();
        await pc.setLocalDescription(offer);
        const response = await fetch('/offer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                sdp: pc.localDescription.sdp,
                type: pc.localDescription.type
            })
        });
        const answer = await response.json();
        await pc.setRemoteDescription(new RTCSessionDescription(answer));
    } catch (error) {
        console.error("Error creating offer:", error);
    }
}

createOffer();