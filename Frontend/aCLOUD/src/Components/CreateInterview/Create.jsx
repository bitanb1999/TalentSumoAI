import React, { useState } from "react";
import styles from "./Create.module.css";

import { useNavigate } from "react-router-dom";

import Quesans from "../Modal/QuesAns";
import Skills from "../Modal/Skills";

import axios from "axios";

const Create = () => {
  const navigate = useNavigate();

  const [disabled, setDisabled] = useState(false);
  const [certificate, setCertificate] = useState(false);
  const [create, setCreate] = useState([]);

  const handleCertificate = () => {
    setCertificate(!certificate);
    setDisabled(!disabled);
  };

  const handleClick = (e) => {
    e.preventDefault();
    navigate("/notification&message");
    axios
      .post(
        "response.json",
        {
          institute_name: create.institute_name,
          job_title: create.job_title,
          test_code: create.test_code,
          track: create.track,
          interaction_mode: create.interaction_mode,
          generate_certificate: create.generate_certificate,
          generate_certificate_text: create.generate_certificate_text,
          job_instruction: create.job_instruction,
          job_description: create.job_description,
          access_code: create.access_code,
          expiry_date: create.expiry_date
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
      <div className="container my-5">
        <div className="d-grid col-md-9 mx-auto">
          <div className="card border-dark">
            <h3
              className={`${styles.cardHeader} card-header text-center mb-3 bg-dark text-white`}
            >
              Create Interaction
            </h3>
            <div className="card-body">
              <form>
                <div className="row">
                  <div className="col-md-4">
                    <div className="mb-3">
                      <label
                        htmlFor="institute_name"
                        className="form-label fw-bold"
                      >
                        Company/Institute Name*
                      </label>
                      <input
                        type="text"
                        onChange={handleOnChange}
                        name="institute_name"
                        value={create.institute_name}
                        className="form-control"
                        placeholder="Enter company/institute name"
                        id="institute_name"
                      />
                    </div>
                  </div>
                  <div className="col-md-4">
                    <div className="mb-3">
                      <label htmlFor="job_title" className="form-label fw-bold">
                        Interaction Title*
                      </label>
                      <input
                        type="text"
                        onChange={handleOnChange}
                        name="job_title"
                        value={create.job_title}
                        className="form-control"
                        placeholder="Enter Interaction title"
                        id="job_title"
                      />
                    </div>
                  </div>
                  <div className="col-md-4">
                    <div className="mb-3">
                      <label htmlFor="test_code" className="form-label fw-bold">
                        Test ID
                      </label>
                      <input
                        type="number"
                        onChange={handleOnChange}
                        name="test_code"
                        value={create.test_code}
                        className="form-control"
                        placeholder="Enter 6-digit code"
                        id="test_code"
                      />
                    </div>
                  </div>
                </div>
                <div className="row">
                  <div className="col-md-6">
                    <div className="mb-3">
                      <label htmlFor="track" className="form-label fw-bold">
                        Track/Domain :
                      </label>
                      <select
                        className="form-select"
                        id="track"
                        onChange={handleOnChange}
                        name="track"
                        value={create.track}
                        aria-label="Default select example"
                      >
                        <option value="Select...">Select...</option>
                        <option value="Sales">Sales</option>
                        <option value="Service">Service</option>
                        <option value="HR">HR</option>
                        <option value="New Grad.">New Grad.</option>
                      </select>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="mb-3">
                      <label htmlFor="interaction_mode" className="form-label fw-bold">
                        Interaction Mode
                      </label>
                      <select
                        className="form-select"
                        id="interaction_mode"
                        onChange={handleOnChange}
                        name="interaction_mode"
                        value={create.interaction_mode}
                        aria-label="Default select example"
                      >
                        <option value="Select">Select...</option>
                        <option value="Audio">Audio</option>
                        <option value="Video">Video</option>
                        <option value="MCQ">MCQ</option>
                        <option value="Image">Image</option>
                        <option value="Text">Text</option>
                      </select>
                    </div>
                  </div>
                </div>
                <div className="row">
                  <div className="col-md-6">
                    <div className="mb-3">
                      <label
                        htmlFor="access_code"
                        className="form-label fw-bold"
                      >
                        Access Code
                      </label>
                      <input
                        type="number"
                        className="form-control"
                        placeholder="Enter 6-digit access code"
                        id="access_code"
                        onChange={handleOnChange}
                        name="access_code"
                        value={create.access_code}
                        aria-describedby="accessHelp"
                      />
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="mb-3">
                      <label
                        htmlFor="expiry_date"
                        className="form-label fw-bold"
                      >
                        Expiry Date
                      </label>
                      <input
                        type="date"
                        className="form-control"
                        id="expiry_date"
                        onChange={handleOnChange}
                        name="expiry_date"
                        value={create.expiry_date}
                      />
                    </div>
                  </div>
                </div>
                <div className="mb-3">
                  <label className="form-label fw-bold">
                    Generate Certificate
                  </label>
                  <div className="d-flex gap-3">
                    <div className="form-check">
                      <input
                        disabled={certificate ? false : true}
                        onClick={handleCertificate}
                        className="form-check-input"
                        type="radio"
                        id="no"
                        onChange={handleOnChange}
                        name="generate_certificate"
                        value="no"
                        defaultChecked
                      />
                      <label className="form-check-label" htmlFor="no">
                        No
                      </label>
                    </div>
                    <div className="form-check">
                      <input
                        disabled={certificate ? true : false}
                        onClick={handleCertificate}
                        className="form-check-input"
                        type="radio"
                        id="yes"
                        onChange={handleOnChange}
                        name="generate_certificate"
                        value="yes"
                      />
                      <label className="form-check-label" htmlFor="yes">
                        Yes
                      </label>
                      {certificate && (
                        <input
                          type="text"
                          className="form-control mt-2 mb-3"
                          id="generate_certificate_text"
                          placeholder="Certificate Name"
                          onChange={handleOnChange}
                        name="generate_certificate_text"
                        value={create.generate_certificate_text}
                        />
                      )}
                    </div>
                  </div>
                </div>
                <div className="row">
                  <div className="col-md-6">
                    <div className="mb-3">
                      <label
                        htmlFor="job_instruction"
                        className="form-label fw-bold"
                      >
                        Instruction
                      </label>
                      <input
                        type="text"
                        className="form-control"
                        placeholder="Your instruction"
                        id="job_instruction"
                        onChange={handleOnChange}
                        name="job_instruction"
                        value={create.job_instruction}
                      />
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="mb-3">
                      <label
                        htmlFor="job_description"
                        className="form-label fw-bold"
                      >
                        Description
                      </label>
                      <input
                        type="text"
                        className="form-control"
                        placeholder="Your description"
                        id="job_description"
                        onChange={handleOnChange}
                        name="job_description"
                        value={create.job_description}
                      />
                    </div>
                  </div>
                </div>
                <div className="row">
                  <div className="col-md-6 m-auto">
                    <div className="d-flex justify-content-between mb-3">
                      <label htmlFor="question" className="form-label fw-bold">
                        Skills:{" "}
                        <span className="badge badge bg-secondary">
                          skill name
                        </span>
                      </label>
                      <button
                        type="button"
                        className="btn btn-outline-secondary button"
                        data-bs-toggle="modal"
                        data-bs-target="#exampleModal1"
                      >
                        Add
                      </button>
                    </div>
                  </div>
                  <div className="col-md-6 m-auto">
                    <div className="d-flex justify-content-between mb-3">
                      <label htmlFor="question" className="form-label fw-bold">
                        Total Question:{" "}
                        <span className="badge badge bg-secondary">No.</span>
                      </label>
                      <button
                        type="button"
                        className="btn btn-outline-secondary button"
                        data-bs-toggle="modal"
                        data-bs-target="#exampleModal"
                      >
                        Add
                      </button>
                    </div>
                  </div>
                </div>
              </form>
              <hr />
              <div className="d-grid col-3 ms-auto">
                <button
                  onClick={handleClick}
                  type="submit"
                  className="btn btn-dark button"
                >
                  Save and Continue
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <Quesans />
      <Skills />
    </>
  );
};

export default Create;