import React, {useEffect, useState} from "react";
import CustomTable from "../GenericComponents/Table/customTable";
import {useDispatch, useSelector} from "react-redux";
import LoadingSpinner from "../GenericComponents/loadingSpinner";
import TimeFrameSelectorForSalesAnalytics from "./timeFrameSelectorForSalesAnalytics";
import {
    getAgentsTable,
    getInboundTable,
    getPartnerTable,
    getUTMTable
} from "../../Util/TableHelpers/salesAnalyticsTableHelper";
import {getSalesAnalyticsData} from "../../Actions/salesAnalyticsAction";
import SalesAnalyticsCards from "./salesAnalyticsCards";

export const SALES_ANALYTICS_WRAPPER = "SALES_ANALYTICS_WRAPPER";
export const agentsTableHeaders = [
    'Upgrade Date',
    'Days Since Creation',
    'Company Name',
    'Company Email',
    'Admin Name',
    'Admin Phone',
    'Assigned To',
    'Current Plan',
    'Country',
];

export const inboundTableHeaders = [
    'Upgrade Date',
    'Days Since Creation',
    'Company Name',
    'Company Email',
    'Admin Name',
    'Admin Phone',
    'Current Plan',
    'Country',
];

export const partnerTableHeaders = [
    'Upgrade Date',
    'Days Since Creation',
    'Company Name',
    'Company Email',
    'Admin Name',
    'Admin Phone',
    'Current Plan',
    'Partner Email',
    'Country',
];

export const utmTableHeaders = [
    'Upgrade Date',
    'Days Since Creation',
    'Company Name',
    'Company Email',
    'Admin Name',
    'Admin Phone',
    'Current Plan',
    'Country',
    'UTM Parameters'
];


let controller = null;
const SalesAnalyticsWrapper = () => {
    const salesAnalytics = useSelector(state => state.salesAnalytics);

    const dispatch = useDispatch();
    const [selectedTime, setSelectedTime] = useState('thisWeek');
    const [selectedInd, setSelectedInd] = useState(0);
    const [showLoad, setShowLoad] = useState(false);

    useEffect(() => {
        setShowLoad(true);
        if (controller) controller.abort();

        controller = new AbortController();
        dispatch(getSalesAnalyticsData(selectedTime, controller));
    }, [dispatch, selectedTime]);

    useEffect(() => {
        setShowLoad(false);
    }, [salesAnalytics]);

    if (salesAnalytics === null) {
        return <LoadingSpinner/>;
    }

    const agentsBodyArr = getAgentsTable(salesAnalytics?.ae);
    const inboundBodyArr = getInboundTable(salesAnalytics?.inbound);
    const partnerBodyArr = getPartnerTable(salesAnalytics?.partner);
    const utmBodyArr = getUTMTable(salesAnalytics?.utm);

    const getChildren = () => {
        switch (selectedInd) {
            case 1:
                return (
                    <div className="mt-1 salesTableHeight inboundTableWrapper">
                        <CustomTable
                            filterString={""}
                            tableHeaderArr={inboundTableHeaders}
                            tableBodyArr={inboundBodyArr}
                            errorText={"No data available"}
                            showSearch={true}
                            option={{enableClickOnRow: false}}
                            positionPagingAtBottom={true}
                            searchFloatLeft={true}
                        />
                        {showLoad && <LoadingSpinner/>}
                    </div>
                )

            case 2:
                return (
                    <div className="mt-1 salesTableHeight partnerTableWrapper">
                        <CustomTable
                            filterString={""}
                            tableHeaderArr={partnerTableHeaders}
                            tableBodyArr={partnerBodyArr}
                            errorText={"No data available"}
                            showSearch={true}
                            option={{enableClickOnRow: false}}
                            positionPagingAtBottom={true}
                            searchFloatLeft={true}
                        />
                        {showLoad && <LoadingSpinner/>}
                    </div>
                );

            case 3:
                return (
                    <div className="mt-1 salesTableHeight utmTableWrapper">
                        <CustomTable
                            filterString={""}
                            tableHeaderArr={utmTableHeaders}
                            tableBodyArr={utmBodyArr}
                            errorText={"No data available"}
                            showSearch={true}
                            option={{enableClickOnRow: false}}
                            positionPagingAtBottom={true}
                            searchFloatLeft={true}
                        />
                        {showLoad && <LoadingSpinner/>}
                    </div>
                );

            default:
                return (
                    <div className="mt-1 salesTableHeight salesTableWrapper">
                        <CustomTable
                            filterString={""}
                            tableHeaderArr={agentsTableHeaders}
                            tableBodyArr={agentsBodyArr}
                            errorText={"No data available"}
                            showSearch={true}
                            option={{enableClickOnRow: false}}
                            positionPagingAtBottom={true}
                            searchFloatLeft={true}
                        />
                        {showLoad && <LoadingSpinner/>}
                    </div>

                )
        }
    }

    return (
        <div className={`mx-4 bg-white rounded p-2 pb-0 ${showLoad ? "div-loading" : ""}`}>
            <div className="d-flex flex-column">
                <TimeFrameSelectorForSalesAnalytics selectedTime={selectedTime} setSelectedTime={setSelectedTime}/>
                <div className="d-flex justify-content-around mt-3 gap-2">
                    <SalesAnalyticsCards title="Agents" count={agentsBodyArr.length} selected={selectedInd === 0} onClick={() => setSelectedInd(0)}/>
                    <SalesAnalyticsCards title="Inbound" count={inboundBodyArr.length} selected={selectedInd === 1} onClick={() => setSelectedInd(1)}/>
                    <SalesAnalyticsCards title="Partners" count={partnerBodyArr.length} selected={selectedInd === 2} onClick={() => setSelectedInd(2)}/>
                    <SalesAnalyticsCards title="Ads" count={utmBodyArr.length} selected={selectedInd === 3} onClick={() => setSelectedInd(3)}/>
                </div>
                <div className="mt-3">
                    {getChildren()}
                </div>
            </div>
        </div>
    );
};

export default SalesAnalyticsWrapper;
