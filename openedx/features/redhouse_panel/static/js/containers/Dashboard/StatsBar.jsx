import React, { useState, useEffect } from "react";
import { Card } from "reactstrap";
import StatsBox from "./StatsBox";
import Loader from "../../common/components/Loader";

import UserApiClient from "../../lib/api/usersApi";

export default function StatsBar(props) {
    const [isLoading, setIsLoading] = useState(true);
    const [stats, setStats] = useState({
        instructorCount: 0,
        studentCount: 0,
    });

    async function setUserStats() {
        const stats = await UserApiClient.getAccountsStats();
        setStats(stats);
        setIsLoading(false);
    }
    useEffect(() => {
        setUserStats();
    }, []);
    return (
        <Card>
            {isLoading ? (
                <Loader />
            ) : (
                <ul className="stats-list">
                     <Loader />
                    <li>
                        <StatsBox number={stats.instructorCount} text={"Teachers/Admins"} />
                    </li>
                    <li>
                        <StatsBox number={stats.studentCount} text={"Student Accounts"} />
                    </li>
                    <li>
                        <StatsBox number={"1,000"} text={"Public Accounts"} />
                    </li>
                </ul>
            )}
        </Card>
    );
}
