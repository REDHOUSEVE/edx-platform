/**
 * Constants API URLs.
 */

/**
 * BASE URLs
 */
export const API_BASE = '/redhouse-panel/api/v0';

/**
 * Utils
 */

const apiUrl = url => `${API_BASE}${url}`

/**
 * User related APIs
 */
export const USER_ACCOUNT_STATS = apiUrl('/account_stats');

/**
 * Site related APIs
 */

export const SITE_INFO = apiUrl('/site/1');
