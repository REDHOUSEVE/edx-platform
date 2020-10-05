import React, { useContext } from "react";

import { SiteContext } from "../siteContext";

export default function useSiteContext() {
    return useContext(SiteContext);
}
