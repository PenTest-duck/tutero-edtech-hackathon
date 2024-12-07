import React, { useEffect, useRef, useState } from "react";

const WebcamFeed = () => {
  const videoRef = useRef<HTMLVideoElement>(null);
  const [key, setKey] = useState(0); // State to force re-render

  useEffect(() => {
    const video = videoRef.current;
    if (video) {
      const tryPlayVideo = () => {
        video.muted = true;
        video
          .play()
          .then(() => {
            setTimeout(() => {
              video.muted = false;
            }, 100);
          })
          .catch((error) => {
            console.error("Error attempting to play the video:", error);
            setTimeout(tryPlayVideo, 1000); // Retry after 1 second
          });
      };

      tryPlayVideo();

      const handleVideoEnd = () => {
        setKey((prevKey) => prevKey + 1); // Update key to re-render component
      };

      video.addEventListener("ended", handleVideoEnd);

      return () => {
        video.removeEventListener("ended", handleVideoEnd);
      };
    }
  }, [key]);

  return (
    <div key={key} className="bg-card text-card-foreground rounded-lg shadow-lg p-4 aspect-video relative">
      <div className="absolute inset-0 flex items-center justify-center">
        <video ref={videoRef} autoPlay playsInline className="w-full h-full" controls>
          <source src="downloaded_video.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>
    </div>
  );
};

export default WebcamFeed;
