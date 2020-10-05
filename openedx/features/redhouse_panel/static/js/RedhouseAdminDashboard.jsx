import React from "react";
import ReactDOM from "react-dom";

import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import PanelNavbar from "./containers/Navbar";
import Dashboard from "./containers/Dashboard";

import { SiteContext } from "./common/siteContext";

export default function AdminPanel({ context }) {
    return (
        <SiteContext.Provider value={context}>
            <Router basename={context.base_url}>
                <PanelNavbar />
                <Switch>
                    <Route exact path="/" component={Dashboard} />
                    <Route path="/people">
                        <div>People Page</div>
                    </Route>
                    <Route path="/settings">
                        <div>Settings Page</div>
                    </Route>
                </Switch>
            </Router>
        </SiteContext.Provider>
    );
}

export class RedhouseAdminDashboard {
    constructor(context) {
        ReactDOM.render(<AdminPanel context={context} />, document.getElementById("root"));
    }
}
