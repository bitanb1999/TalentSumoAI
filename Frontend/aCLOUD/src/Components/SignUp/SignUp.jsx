import React, { useState } from "react";
import styles from "./SignUp.module.css";
import { useNavigate } from "react-router-dom";

import { IoIosLock } from "react-icons/io";

import welcome from "../../assets/Images/signup.png";

import axios from "axios";

const SignUp = () => {
  const navigate = useNavigate();
  const [create, setCreate] = useState([]);

  const handleClick = (e) => {
    e.preventDefault();
    navigate("/");
    axios
      .post(
        "response.json",
        {
          firstName: create.firstName,
          lastName: create.lastName,
          username: create.username,
          email: create.email,
          password: create.password,
          confirmPassword: create.confirmPassword,
          invitationCode: create.invitationCode,
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
      <div className="container mt-5">
        <div className="row">
          <div
            className={`${styles.left} col-md-6 d-flex justify-content-center m-auto`}
          >
            <img
              className={`${styles.img} img-fluid`}
              src={welcome}
              alt="welcome"
            />
          </div>
          <div className="col-md-6 m-auto">
            <div className="card border-dark">
              <div className="card-body">
                <h3 className="text-dark">Sign Up</h3>
                <p className="text-muted">
                  Please fill in this form to create an account!
                </p>
                <hr
                  style={{
                    color: "#000",
                    borderTop: "2px solid",
                    opacity: "1",
                  }}
                />
                <form className="mt-5">
                  <div className="row">
                    <div className="col-md-6">
                      <div className="mb-3">
                        <input
                          type="text"
                          className="form-control"
                          id="firstName"
                          onChange={handleOnChange}
                        name="firstName"
                        value={create.firstName}
                          placeholder="First Name"
                        />
                      </div>
                    </div>
                    <div className="col-md-6">
                      <div className="mb-3">
                        <input
                          type="text"
                          className="form-control"
                          id="lastName"
                          onChange={handleOnChange}
                        name="lastName"
                        value={create.lastName}
                          placeholder="Last Name"
                        />
                      </div>
                    </div>
                  </div>
                  <div className="mb-3">
                    <input
                      type="text"
                      className="form-control"
                      id="username"
                      onChange={handleOnChange}
                        name="username"
                        value={create.username}
                      placeholder="Username"
                    />
                  </div>
                  <div className="mb-3">
                    <input
                      type="email"
                      className="form-control"
                      id="email"
                      placeholder="Email"
                    />
                  </div>
                  <div className="mb-3">
                    <input
                      type="password"
                      className="form-control"
                      id="password"
                      onChange={handleOnChange}
                        name="password"
                        value={create.password}
                      placeholder="Password"
                    />
                  </div>
                  <div className="mb-3">
                    <input
                      type="password"
                      className="form-control"
                      id="confirmPassword"
                      onChange={handleOnChange}
                        name="confirmPassword"
                        value={create.confirmPassword}
                      placeholder="Confirm Password"
                    />
                  </div>
                  <div className="mb-3">
                    <input
                      type="number"
                      className="form-control"
                      id="inviteCode"
                      onChange={handleOnChange}
                        name="invitationCode"
                        value={create.invitationCode}
                      placeholder="Invitation Code"
                    />
                  </div>
                  <div className="mb-3 d-grid col-4 mx-auto">
                    <button
                      type="button"
                      onClick={handleClick}
                      className="btn btn-dark"
                    >
                      <IoIosLock className="fs-4 me-1" />
                      Create Account
                    </button>
                  </div>
                  <p className={`${styles.new} text-center`}>
                    Already have an account ?{" "}
                    <span
                      onClick={() => navigate("/login")}
                      className="ms-1 text-dark fw-bold text-decoration-underline"
                      style={{ cursor: "pointer" }}
                    >
                      Login here
                    </span>
                  </p>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default SignUp;
