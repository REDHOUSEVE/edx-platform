import React from "react";

import { Card, CardBody, CardTitle, CardText, Col, Row } from "reactstrap";

import useSiteContext from "../../common/hooks/useSiteContext";

export default function UserDetails(props) {
    const context = useSiteContext();
    return (
        <Card>
            <CardTitle>
                <h2>Lead Admin</h2>
            </CardTitle>
            <CardBody>
                <img
                    className="img-round"
                    src="https://sms.northhills.edu.pk/uploads/website/officers/anonymous-user.png"
                />
                <Col>
                    <ul>
                        <li>
                            <span className="title">Name</span>
                            <span className="text">{context.user.username}</span>
                        </li>
                        <li>
                            <span className="title">Email Address</span>
                            <span className="text">{context.user.email}</span>
                        </li>
                        <li>
                            <span className="title">Phone Number</span>
                            <span className="text">+12147775555</span>
                        </li>
                    </ul>
                </Col>
            </CardBody>
        </Card>
    );
}
