import React from "react";

const WebcamFeed = () => {
  return (
    <div className="bg-card text-card-foreground rounded-lg shadow-lg p-4 aspect-video relative">
      <div className="absolute inset-0 flex items-center justify-center">
        {/* <p className="text-muted-foreground">Webcam feed will appear here</p> */}
        <video autoPlay playsInline className="w-full h-full" src="@/assets/video/downloaded_video.mp4"></video>
      </div>
    </div>
  );
};

export default WebcamFeed;
