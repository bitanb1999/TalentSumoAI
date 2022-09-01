import React from "react";
import styles from "./InteractionTranscript.module.css";

const InteractionTranscript = () => {
  return (
    <>
      <div className="container">
        <h3 className='text-center mb-5' style={{ color: "#0b3c47" }}>INTERACTION TRANSCRIPT <span className="badge bg-danger">Experimental</span></h3>
        <h5>Question : 1 Are you comfortable making cold calls?</h5>
        <div className={styles.para}>
          I am—yes. The results can be unpredictable when you pick up the phone, but I find that doing research on the person and the company can help make
          this type of call successful. I had great success with this tactic during my time at ABC Company.
        </div>
        <h5>Question : 2 Have you consistently met your sales goals?</h5>
        <div className={styles.para}>
          At XY Tech, I've been one of the top salespeople in the department for the past six quarters. Prior to that, I had one really rough quarter.
          I was discouraged, but then realized it was an opportunity to re-think my strategy, and it's been really exciting to see those adjustments have
          such a positive payoff.
        </div>
        <h5>Question : 3 What motivates you?</h5>
        <div className={styles.para}>
          Every quarter, I strive to go beyond my quota and compete with my personal best results from previous periods. My goal is always to see growth in my
          sales records with each new quarter.
        </div>
        <h5>Question : 4 Sell me this pen.</h5>
        <div className={styles.para}>
          Even in our tech-focused world, a pen is still essential. What I like about this one is that it has a secure cap so it won't stain pocket interiors
          or a bag. Plus, it's refined-looking yet still budget friendly.
        </div>
      </div>
    </>
  );
};

export default InteractionTranscript;
