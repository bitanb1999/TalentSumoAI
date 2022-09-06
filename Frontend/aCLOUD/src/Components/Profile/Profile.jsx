import React, { useState } from "react";
import styles from "./Profile.module.css";
import Profilepic from "./Profilepic";
import { FaUser, FaPenSquare } from "react-icons/fa";

import axios from "axios";

import { countries } from "../../assets/Countries/countries";

const Profile = () => {
  const [style, setStyle] = useState({ display: "none" });
  const [create, setCreate] = useState([]);

  const mouseEnter = () => {
    setStyle({
      display: "block",
      width: "15%",
      height: "15%",
      position: "absolute",
      left: "60%",
      top: "25%",
      cursor: "pointer",
    });
  };
  const mouseLeave = () => {
    setStyle({
      display: "none",
    });
  };

  const handleSubmit = () => {
    axios
      .post(
        "response.json",
        {
          firstName: create.firstName,
          lastName: create.lastName,
          email: create.email,
          phoneNumber: create.phoneNumber,
          companyName: create.companyName,
          country: create.country,
          linkedIn: create.linkedIn,
          facebook: create.facebook,
          twitter: create.twitter,
          instagram: create.instagram,
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
      <div className="mt-5 container">
        <div className="row">
          <div className="col-md-5 mx-auto">
            <div className={`${styles.card} card`}>
              <div className="card-body">
                <h5>Upload Profile Picture :</h5>
              </div>
              <div className="card-body d-flex justify-content-center">
                {/* <div className="mb-3">
                                    <label htmlFor="formFile" className="form-label">Upload Profile Picture</label>
                                    <input className="form-control" type="file" id="formFile" />
                                </div> */}
                {/* <button  className='btn btn-dark button'>Upload</button> */}
                <FaUser
                  onMouseEnter={mouseEnter}
                  onMouseLeave={mouseLeave}
                  className="h-50 w-50 m-auto p-3 bg-light"
                />
                <FaPenSquare
                  style={style}
                  onMouseEnter={mouseEnter}
                  data-bs-toggle="modal"
                  data-bs-target="#exampleModal"
                />
              </div>
            </div>
          </div>
          <div className="col-md-7">
            <div className={`${styles.card} card`}>
              <div className="card-body">
                <div className="d-flex justify-content-between">
                  <h5 className="card-title">Personal Details :</h5>
                  <div className="text-end">
                    <button className="btn btn-secondary button">Edit</button>
                    <p className="text-danger">Click Edit to update details*</p>
                  </div>
                </div>
                <div className="row">
                  <div className="col-md-6">
                    <div className="mb-3">
                      <input
                        type="text"
                        className="form-control"
                        id="fName"
                        placeholder="First Name"
                        onChange={handleOnChange}
                        value={create.firstName}
                        name="firstName"
                      />
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="mb-3">
                      <input
                        type="text"
                        className="form-control"
                        id="lName"
                        placeholder="Last Name"
                        onChange={handleOnChange}
                        value={create.lastName}
                        name="lastName"
                      />
                    </div>
                  </div>
                </div>
                <div className="row">
                  <div className="col-md-6">
                    <div className="mb-3">
                      <input
                        type="email"
                        className="form-control"
                        id="emailAddress"
                        placeholder="Email address"
                        onChange={handleOnChange}
                        value={create.email}
                        name="email"
                      />
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="mb-3">
                      <input
                        type="number"
                        className="form-control"
                        id="contactNumber"
                        placeholder="Phone Number"
                        onChange={handleOnChange}
                        value={create.phoneNumber}
                        name="phoneNumber"
                      />
                    </div>
                  </div>
                </div>
                <div className="row">
                  <div className="col-md-6">
                    <div className="mb-3">
                      <input
                        type="text"
                        className="form-control"
                        id="companyName"
                        placeholder="Company Name"
                        onChange={handleOnChange}
                        value={create.companyName}
                        name="companyName"
                      />
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="mb-3">
                      <select
                        className="form-select"
                        aria-label="Default select example"
                        onChange={handleOnChange}
                        value={create.country}
                        name="country"
                      >
                        <option value="Select Country">Select Country</option>
                        {countries.map((item) => (
                          <option>{item.name}</option>
                        ))}
                      </select>
                    </div>
                  </div>
                </div>
                <h5 className="card-title mt-4">Social Links :</h5>
                <div className="mb-3">
                  <div className="row">
                    <div className="col-md-6">
                      <div className="mb-3">
                        <input
                          type="text"
                          className="form-control"
                          id="linkedin"
                          placeholder="LinkedIn"
                          onChange={handleOnChange}
                          value={create.linkedIn}
                          name="linkedIn"
                        />
                      </div>
                    </div>
                    <div className="col-md-6">
                      <div className="mb-3">
                        <input
                          type="text"
                          className="form-control"
                          id="facebook"
                          placeholder="Facebook"
                          onChange={handleOnChange}
                          value={create.facebook}
                          name="facebook"
                        />
                      </div>
                    </div>
                  </div>
                  <div className="row">
                    <div className="col-md-6">
                      <div className="mb-3">
                        <input
                          type="text"
                          className="form-control"
                          id="twitter"
                          placeholder="Twitter"
                          onChange={handleOnChange}
                          value={create.twitter}
                          name="twitter"
                        />
                      </div>
                    </div>
                    <div className="col-md-6">
                      <div className="mb-3">
                        <input
                          type="text"
                          className="form-control"
                          id="instagram"
                          placeholder="Instagram"
                          onChange={handleOnChange}
                          value={create.instagram}
                          name="instagram"
                        />
                      </div>
                    </div>
                  </div>

                  <button
                    onClick={handleSubmit}
                    className="btn btn-dark button"
                  >
                    Submit Details
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <Profilepic />
    </>
  );
};

export default Profile;
