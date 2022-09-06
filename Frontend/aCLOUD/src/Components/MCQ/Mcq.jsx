import React, { useState } from "react";
import styles from "./Mcq.module.css";
import { useNavigate } from "react-router-dom";

import mcq from "../../assets/Images/mcq.png";

import axios from "axios";

const Mcq = () => {
  const navigate = useNavigate();
  const [create, setCreate] = useState([]);

  const next = () => {
    navigate("/imageUpload");
    axios
      .post(
        "response.json",
        {
          collect_questions: create.collect_questions,
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
          <div className="col-md-4 bg-dark">
            <img
              className="d-flex justify-content-center mx-auto img-fluid m-auto p-3"
              width={300}
              src={mcq}
              alt="mcq"
            />
          </div>
          <div className="col-md-8 m-auto">
            <div className="container my-3">
              <h4>Question ?</h4>
              <hr />
              <div className="form-check">
                <input
                  className="form-check-input"
                  type="radio"
                  name="collect_questions"
                  onChange={handleOnChange}
                value="option1"
                  id="option1"
                />
                <label className="form-check-label" htmlFor="option1">
                  Option 1
                </label>
              </div>
              <div className="form-check">
                <input
                  className="form-check-input"
                  type="radio"
                  name="collect_questions"
                  onChange={handleOnChange}
                value="option2"
                  id="option2"
                />
                <label className="form-check-label" htmlFor="option2">
                  Option 2
                </label>
              </div>
              <div className="form-check">
                <input
                  className="form-check-input"
                  type="radio"
                  name="collect_questions"
                  onChange={handleOnChange}
                value="option3"
                  id="option3"
                />
                <label className="form-check-label" htmlFor="option3">
                  Option 3
                </label>
              </div>
              <div className="form-check">
                <input
                  className="form-check-input"
                  type="radio"
                  name="collect_questions"
                  onChange={handleOnChange}
                value="option4"
                  id="option4"
                />
                <label className="form-check-label" htmlFor="option4">
                  Option 4
                </label>
              </div>
              <hr />
              <button onClick={next} className="btn btn-dark float-end mb-3">
                Save and Next
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Mcq;
