import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000';

export const addUser = async (name: string, gender: string) => {
    try {
        const response = await axios.post(`${API_URL}//add_user`, { name, gender });
        return response.data;
    } catch (error) {
        console.error('Error adding user:', error);
        throw error;
    }
};

export const getUsers = async (page: number) => {
    try {
        const response = await axios.get(`${API_URL}/get_user_list`, { params: { page } });
        return response.data;
    } catch (error) {
        console.error('Error getting users:', error);
        throw error;
    }
};

export const editUser = async (id: string, name: string, gender: string) => {
    try {
        const response = await axios.put(`${API_URL}/edit_user/${id}`, { name, gender });
        return response.data;
    } catch (error) {
        console.error('Error editing user:', error);
        throw error;
    }
};