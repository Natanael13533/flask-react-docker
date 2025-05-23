// components/PublicRoute.js
import React from "react";
import { Navigate } from "react-router-dom";

const PublicRoute = ({ children }) => {
  const token = localStorage.getItem("access_token");
  return token ? <Navigate to="/" /> : children;
};

export default PublicRoute;
