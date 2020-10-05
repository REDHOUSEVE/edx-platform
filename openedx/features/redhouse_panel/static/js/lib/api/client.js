import axios from 'axios';

export default {
    async get(url) {
        return (await axios.get(url)).data;
    },

    async post(url, data) {
        return (await axios.post(url, data)).data;
    },

    async put(url, data) {
        return (await axios.put(url, data)).data;
    },

    async delete(url, data) {
        return (await axios.delete(url)).data;
    },
}
