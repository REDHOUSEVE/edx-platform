import React, { useEffect, useState } from "react";

import { Card, CardBody, CardTitle, CardText, Col, Row } from "reactstrap";

import Loader from "../../common/components/Loader";

import SitesApiClient from "../../lib/api/sitesApi";

export default function SchoolInfo(props) {
    const [isLoading, setIsLoading] = useState(true);
    const [siteInfo, setSiteInfo] = useState({
        name: null,
        address: null,
    });
    async function displaySiteInfo() {
        const data = await SitesApiClient.getSiteInfo();
        setSiteInfo(data);
        setIsLoading(false);
        console.log(data);
    }
    useEffect(() => {
        displaySiteInfo();
    }, []);

    return (
        <Card>
            {isLoading ? (
                <Loader />
            ) : (
                <div>
                    <CardTitle>
                        <h2>School Information</h2>
                    </CardTitle>
                    <CardBody>
                        <img src="https://sms.northhills.edu.pk/uploads/website/officers/anonymous-user.png" />
                        <Col>
                            <ul>
                                <li>
                                    <span className="title">Name</span>
                                    <span className="text">{siteInfo.name || "N/A"}</span>
                                </li>
                                <li>
                                    <span className="title">Address</span>
                                    <span className="text">{siteInfo.address || "N/A"}</span>
                                </li>
                            </ul>
                        </Col>
                    </CardBody>
                </div>
            )}
        </Card>
    );
}
