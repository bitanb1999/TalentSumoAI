import React, { useState } from "react";
import styles from "./Text.module.css";
import { useNavigate } from "react-router-dom";

import axios from "axios";

import text from "../../assets/Images/text.svg";

const Text = () => {
  const navigate = useNavigate();
  const [create, setCreate] = useState([]);

  const handleSave = () => {
    navigate("/thanks");
    axios
      .post(
        "response.json",
        {
          answer: create.answer,
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
      <div className={`${styles.container} container my-5`}>
        <div className="row">
          <div className={`${styles.left} col-md-4`}>
            <img
              className="d-flex justify-content-center mx-auto img-fluid m-auto"
              width={300}
              src={text}
              alt="writeyouranswer"
            />
          </div>
          <div className="col-md-8 m-auto">
            <div className="container my-3">
              <h4>Question ?</h4>
              <hr />
              <textarea
                className="form-control"
                onChange={handleOnChange}
                value={create.answer}
                name="answer"
                id="exampleFormControlTextarea1"
                placeholder="Write your answer"
                rows="3"
              ></textarea>
              <hr />
              <button onClick={handleSave} className="btn btn-dark float-end">
                Save and Next
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Text;
