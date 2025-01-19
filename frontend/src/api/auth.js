import apiClient from "./apiClient";

export const login = async (username, password) => {
  const response = await apiClient.post("/auth/login", { username, password });
  if (response.data.access_token) {
    localStorage.setItem("token", response.data.access_token);
  }
  return response.data;
};

export const logout = () => {
  localStorage.removeItem("token");
};

export const getCurrentUser = async () => {
  const response = await apiClient.get("/auth/me");
  return response.data;
};
