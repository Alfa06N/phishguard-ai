import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

api.interceptors.response.use(
  (response) => response.data,
  (error) => {
    console.log(error.response);
    if (error.response) {
      const standardizedError = {
        status: error.response.status,
        message: error.response.data.detail || "An error occurred",
        type: error.response.type || "API_ERROR",
      };
      return Promise.reject(standardizedError);
    }

    const networkError = {
      status: 503,
      message: "Cannot reach the security server. Check your connection.",
      type: "NETWORK_ERROR",
    };
    return Promise.reject(networkError);
  },
);

export default api;
