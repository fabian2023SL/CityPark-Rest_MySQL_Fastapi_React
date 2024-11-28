import axios from "axios";

const axiosInstance = axios.create({
    baseURL: process.env.API_URL || "http://localhost:2000",
    mode : "no-cors",
	headers: {
      "Content-Type": "application/json", 
    } 
})

export default axiosInstance;