// src/api/auth.js
import axios from 'axios';

// Base URL from environment variable
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';

// Signup request
export const signup = async (userData) => {
    const response = await axios.post(`${API_URL}/users/signup`, userData);
    return response.data;
};

// Login request
export const login = async (userData) => {
    const response = await axios.post(`${API_URL}/users/login`, userData);
    return response.data;
};

// Fetch profile data (protected route)
export const getProfile = async (token) => {
    const response = await axios.get(`${API_URL}/users/profile`, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    });
    return response.data;
};
