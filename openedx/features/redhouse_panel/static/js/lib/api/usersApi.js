import HttpClient from './client';
import { USER_ACCOUNT_STATS } from './constants';

export default {
    async getAccountsStats() {
        const response = await HttpClient.get(USER_ACCOUNT_STATS);
        return {
            instructorCount: response.instructor_count,
            studentCount: response.student_count
        };
    }
}
