import React, { useState } from "react";
import styles from "./Notification.module.css";
import { useNavigate } from "react-router-dom";

import { FaTelegram, FaWhatsapp, FaSlack, FaWpforms } from "react-icons/fa";

import axios from "axios";

const Notification = () => {
  const navigate = useNavigate();

  const handleBack = (e) => {
    e.preventDefault();
    navigate("/create");
  };
  
  const [isNeeded, setIsNeeded] = useState(false);
  const [disabled, setDisabled] = useState(false);
  const [create, setCreate] = useState([]);

  const handleNeeded = () => {
    setIsNeeded(!isNeeded);
    setDisabled(!disabled);
  };

  const handleSubmit = () => {
    navigate("/thankyou");
    axios
      .post(
        "response.json",
        {
          interaction_welcome_message: create.interaction_welcome_message,
          interaction_instruction_message:
            create.interaction_instruction_message,
          interaction_completion_message: create.interaction_completion_message,
          bot_warning_message: create.bot_warning_message,
          report_send_to_user: create.report_send_to_user,
          report_send_to_email_one: create.report_send_to_email_one,
          report_send_to_email_two: create.report_send_to_email_two,
        },
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
        }
      )
      .then((res) => {
        console.log(res.data);
      });
  };


  const handleOnChange = (e) => {
    setCreate({ ...create, [e.target.name]: e.target.value });
  };


  return (
    <>
      <style jsx="true">
        {`
          .button {
            border-radius: 0;
          }
        `}
      </style>
      <div className="container mt-5 mb-4">
        <div className="d-flex justify-content-center mx-auto">
          <div className="mb-3">
            <label className="form-label fw-bold">Bot Needed ?</label>
            <div className="d-flex gap-3">
              <div className="form-check">
                <input
                  disabled={isNeeded ? false : true}
                  onClick={handleNeeded}
                  className="form-check-input"
                  type="radio"
                  name="botNeed"
                  id="no"
                  defaultChecked
                />
                <label className="form-check-label" htmlFor="no">
                  No
                </label>
              </div>
              <div className="form-check">
                <input
                  disabled={isNeeded ? true : false}
                  onClick={handleNeeded}
                  className="form-check-input"
                  type="radio"
                  name="botNeed"
                  id="yes"
                />
                <label className="form-check-label" htmlFor="yes">
                  Yes
                </label>
              </div>
            </div>
          </div>
        </div>

        {isNeeded && (
          <div className="card border-dark h-100 mb-3">
            <h3
              className={`${styles.headingNotify} card-header bg-dark text-white text-center`}
            >
              External Bot
            </h3>
            <div className="card-body">
              <form>
                <div className="mb-2">
                  <label htmlFor="phoneNo" className="form-label  fw-bold">
                    Phone Number List
                  </label>
                  <input className="form-control" type="file" id="formFile" />
                </div>
                <button className="btn btn-outline-dark button mb-3 me-2">
                  View List
                </button>
                <button className="btn btn-dark button mb-3">Upload</button>

                <div className="row">
                  <div className="col-md-6">
                    <div className="mb-3">
                      <label
                        htmlFor="whoInitiate"
                        className="form-label fw-bold"
                      >
                        Who can Initiate ?
                      </label>
                      <select className="form-select" id="whoInitiate">
                        <option value="Select">Select...</option>
                        <option value="Bot">Bot</option>
                        <option value="User">User</option>
                      </select>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="mb-3">
                      <label
                        htmlFor="whoInitiate"
                        className="form-label fw-bold"
                      >
                        Timer
                      </label>
                      <select
                        className="form-select"
                        id="whoInitiate"
                        aria-label="Default select example"
                      >
                        <option value="Select">Select...</option>
                        <option value="15 minutes">15 minutes</option>
                        <option value="20 minutes">20 minutes</option>
                        <option value="30 minutes">30 minutes</option>
                        <option value="45 minutes">45 minutes</option>
                        <option value="60 minutes">60 minutes</option>
                      </select>
                    </div>
                  </div>
                </div>

                <div className="row">
                  <div className="col-md-4">
                    <div className="mb-3">
                      <label htmlFor="email" className="form-label fw-bold">
                        Collect Email
                      </label>
                      <div className="form-check">
                        <input
                          className="form-check-input"
                          type="radio"
                          name="collectEmail"
                          id="yes"
                        />
                        <label className="form-check-label" htmlFor="yes">
                          Yes
                        </label>
                      </div>
                      <div className="form-check">
                        <input
                          className="form-check-input"
                          type="radio"
                          name="collectEmail"
                          id="no"
                          defaultChecked
                        />
                        <label className="form-check-label" htmlFor="no">
                          No
                        </label>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-4">
                    <div className="mb-3">
                      <label
                        htmlFor="collectResume"
                        className="form-label fw-bold"
                      >
                        Collect Resume
                      </label>
                      <div className="form-check">
                        <input
                          className="form-check-input"
                          type="radio"
                          name="CollectResume"
                          id="yesResume"
                        />
                        <label className="form-check-label" htmlFor="yesResume">
                          Yes
                        </label>
                      </div>
                      <div className="form-check">
                        <input
                          className="form-check-input"
                          type="radio"
                          name="CollectResume"
                          id="noResume"
                          defaultChecked
                        />
                        <label className="form-check-label" htmlFor="noResume">
                          No
                        </label>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-4">
                    <div className="mb-3">
                      <label
                        htmlFor="feedbackMessage"
                        className="form-label fw-bold"
                      >
                        Candidate Feedback Message
                      </label>
                      <div className="form-check">
                        <input
                          className="form-check-input"
                          type="radio"
                          name="CandidateFeedback"
                          id="yesFeedbackMessage"
                        />
                        <label
                          className="form-check-label"
                          htmlFor="yesFeedbackMessage"
                        >
                          Yes
                        </label>
                      </div>
                      <div className="form-check">
                        <input
                          className="form-check-input"
                          type="radio"
                          name="CandidateFeedback"
                          id="noFeedbackMessage"
                          defaultChecked
                        />
                        <label
                          className="form-check-label"
                          htmlFor="noFeedbackMessage"
                        >
                          No
                        </label>
                      </div>
                    </div>
                  </div>
                </div>

                <div className="row">
                  <div className="col-md-4">
                    <div className="mb-3">
                      <label htmlFor="channel" className="form-label fw-bold">
                        Channel
                      </label>
                      <div className="form-check">
                        <input
                          disabled
                          className="form-check-input"
                          type="checkbox"
                          id="telegram"
                        />
                        <label className="form-check-label" htmlFor="telegram">
                          <FaTelegram
                            className="me-1"
                            style={{ color: "#0088cc" }}
                          />
                          Telegram
                        </label>
                      </div>
                      <div className="form-check">
                        <input
                          disabled
                          className="form-check-input"
                          type="checkbox"
                          id="whatsapp"
                        />
                        <label className="form-check-label" htmlFor="whatsapp">
                          <FaWhatsapp
                            className="me-1"
                            style={{ color: "#25d366" }}
                          />
                          Whatsapp
                        </label>
                      </div>
                      <div className="form-check">
                        <input
                          disabled
                          className="form-check-input"
                          type="checkbox"
                          id="slack"
                        />
                        <label className="form-check-label" htmlFor="slack">
                          <FaSlack
                            className="me-1"
                            style={{ color: "#E01E5A" }}
                          />
                          Slack
                        </label>
                      </div>
                      <div className="form-check mb-3">
                        <input
                          className="form-check-input"
                          type="checkbox"
                          defaultChecked
                          id="form"
                        />
                        <label className="form-check-label" htmlFor="form">
                          <FaWpforms className="me-1" />
                          Form
                        </label>
                      </div>
                    </div>
                  </div>
                  <div className="col-md-4">
                    <div className="mb-3">
                      <label
                        htmlFor="candidateID"
                        className="form-label fw-bold"
                      >
                        Collect Candidate ID
                      </label>
                      <div className="form-check">
                        <input
                          className="form-check-input"
                          type="radio"
                          name="CollectID"
                          id="yesId"
                        />
                        <label className="form-check-label" htmlFor="yesId">
                          Yes
                        </label>
                      </div>
                      <div className="form-check">
                        <input
                          className="form-check-input"
                          type="radio"
                          name="CollectID"
                          id="noId"
                          defaultChecked
                        />
                        <label className="form-check-label" htmlFor="noId">
                          No
                        </label>
                      </div>
                    </div>
                  </div>
                </div>
              </form>
            </div>
          </div>
        )}

        <div className="row">
          <div className="col-md-5">
            <div className="card border-dark">
              <h3
                className={`${styles.headingNotify} card-header bg-dark text-white text-center`}
              >
                Interaction Notification
              </h3>
              <div className="card-body">
                <form>
                  <div className="mb-3">
                    <label htmlFor="report_send_to_email_one" className="form-label fw-bold">
                      Report sent to Email-1
                    </label>
                    <input
                      type="email"
                      className="form-control"
                      id="report_send_to_email_one"
                      onChange={handleOnChange}
                        name="report_send_to_email_one"
                        value={create.report_send_to_email_one}
                    />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="report_send_to_email_two" className="form-label fw-bold">
                      Report sent to Email-2
                    </label>
                    <input
                      type="email"
                      className="form-control"
                      id="report_send_to_email_two"
                      onChange={handleOnChange}
                        name="report_send_to_email_two"
                        value={create.report_send_to_email_two}
                    />
                  </div>
                  <div className="mb-3">
                    <label className="form-label fw-bold" htmlFor="report_send_to_user">
                      Report sent to User
                    </label>
                    <select
                      className="form-select"
                      id="report_send_to_user"
                      onChange={handleOnChange}
                        name="report_send_to_user"
                        value={create.report_send_to_user}
                      aria-label="Default select example"
                    >
                      <option value="Select">Select...</option>
                      <option value="Yes">Yes</option>
                      <option value="No">No</option>
                    </select>
                  </div>
                </form>
              </div>
            </div>
          </div>

          <div className="col-md-7">
            <div className={`${styles.right} card border-dark`}>
              <h3
                className={`${styles.headingMsg} card-header bg-dark text-white text-center`}
              >
                Bot Message
              </h3>
              <div className="card-body">
                <form>
                  <div className="mb-3">
                    <label htmlFor="interaction_welcome_message" className="form-label fw-bold">
                      Interaction Welcome Message
                    </label>
                    <textarea
                      className="form-control interaction"
                      id="interaction_welcome_message"
                      onChange={handleOnChange}
                        name="interaction_welcome_message"
                        value={create.interaction_welcome_message}
                      rows="1"
                    ></textarea>
                  </div>
                  <div className="mb-3">
                    <label htmlFor="interaction_instruction_message" className="form-label fw-bold">
                      Interaction Instruction message
                    </label>
                    <textarea
                      className="form-control interaction"
                      id="interaction_instruction_message"
                      onChange={handleOnChange}
                        name="interaction_instruction_message"
                        value={create.interaction_instruction_message}
                      rows="1"
                    ></textarea>
                  </div>
                  <div className="mb-3">
                    <label htmlFor="interaction_completion_message" className="form-label fw-bold">
                      Interaction Completion Message
                    </label>
                    <textarea
                      className="form-control interaction"
                      id="interaction_completion_message"
                      onChange={handleOnChange}
                        name="interaction_completion_message"
                        value={create.interaction_completion_message}
                      rows="1"
                    ></textarea>
                  </div>
                  <div className="mb-3">
                    <label htmlFor="bot_warning_message" className="form-label fw-bold">
                      Bot Message
                    </label>
                    <textarea
                      className="form-control interaction"
                      id="bot_warning_message"
                      onChange={handleOnChange}
                        name="bot_warning_message"
                        value={create.bot_warning_message}
                      rows="1"
                    ></textarea>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
        <hr />
        <div className="d-flex justify-content-end me-auto gap-3">
          <button
            onClick={handleBack}
            className="btn btn-outline-secondary button"
          >
            Back
          </button>
          <button
            onClick={handleSubmit}
            type="submit"
            className="btn btn-dark button"
          >
            Submit
          </button>
        </div>
      </div>
    </>
  );
};

export default Notification;
