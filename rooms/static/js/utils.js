async function playScreenRecording() {
  try {
    const constraints = {
      video: {
        cursor: "always" | "motion" | "never",
        displaySurface: "application" | "browser" | "monitor" | "window",
      },
    };
    const stream = await navigator.mediaDevices.getDisplayMedia(constraints);
    const videoElement = document.querySelector("#screen");
    stream.getTracks().forEach((track) => {
      peerConnection.addTrack(track, stream);
    });
    videoElement.autoplay = true;
    videoElement.playsInline = true;
    videoElement.muted = true;
    videoElement.srcObject = stream;
    window.stopScreenRecording = () => stopStreamedVideo(videoElement);
  } catch (error) {
    console.error("Error opening video camera.", error);
  }
}
//   playScreenRecording();
