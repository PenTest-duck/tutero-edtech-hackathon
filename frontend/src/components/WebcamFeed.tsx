import React, { useEffect, useRef, useState } from "react";
import { Button } from "@/components/ui/button";

const WebcamFeed = () => {
  const videoRef = useRef<HTMLVideoElement>(null);
  const [key, setKey] = useState(0); // State to force re-render
  const [isPlaying, setIsPlaying] = useState(false); // State to track if video is playing

  useEffect(() => {
    if (isPlaying) {
      const video = videoRef.current;
      if (video) {
        const tryPlayVideo = () => {
          video.muted = true;
          video
            .play()
            .then(() => {
              video.muted = false;
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
    }
  }, [isPlaying, key]);

  const handleStart = () => {
    setIsPlaying(true);
  };

  return (
    <div key={key} className="bg-card text-card-foreground rounded-lg shadow-lg p-4 aspect-video relative">
      <div className="absolute inset-0 flex items-center justify-center">
        {!isPlaying ? (
          <Button onClick={handleStart}>Begin Webcam Feed</Button>
        ) : (
          <video ref={videoRef} autoPlay playsInline className="w-full h-full" controls>
            <source src="downloaded_video.mp4" type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        )}
      </div>
    </div>
  );
};

export default WebcamFeed;
