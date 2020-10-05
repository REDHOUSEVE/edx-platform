import HttpClient from './client';
import { SITE_INFO } from './constants';

export default {
    async getSiteInfo() {
        const { name, address } = await HttpClient.get(SITE_INFO);
        return {
            name, address
        }
    }
}
