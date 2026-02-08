import { useState } from "react";
import { getIntelligenceData } from "../utils/mock-data";

export default function AnalyticsPage({searchQuery}) {
    const [product, setProduct] = useState(false);
    const [competitors, setCompetitors] = useState(false);
    
    const {
  finalExecutiveProductIntelligenceReport = [],
  productIntelligence = []
} = getIntelligenceData() || {};
console.log("Intelligence data in AnalyticsPage:", finalExecutiveProductIntelligenceReport, productIntelligence);

// Safe search
const productIndex = finalExecutiveProductIntelligenceReport.findIndex(
  (p) => p.product_name?.toLowerCase() === searchQuery?.toLowerCase()
);

if (productIndex === -1) {
  return (
    <div className="col-span-3 flex items-center justify-center p-12 text-slate-400">
      No report found for "{searchQuery}"
    </div>
  );
}

const summaryReport = finalExecutiveProductIntelligenceReport[productIndex] || {};
const detailedReport = productIntelligence[productIndex] || {};

// Safe nested defaults
const riskMonitoring = detailedReport.risk_and_sales_monitoring || {};
const strategyRecommendation = detailedReport.strategy_recommendation || {};
const uspAnalysis = detailedReport.usp_analysis || {};

// Since your JSON does NOT have similar_products,
// we fallback to core_competitors from summary
const competitorsList = (summaryReport.core_competitors || []).map((name) => ({
  product_name: name,
  estimated_market_share: "N/A",
  company: "Unknown",
  approval_status: "Unknown"
}));

// Launch strategy comes from summaryReport
const launchStrategyText = summaryReport.launch_strategy_recommendation || "No launch strategy available.";
const marketStrategyMoves = strategyRecommendation.defensive_moves || [];

    
    // Helper for risk color
    const getRiskColor = (score) => {
  if (score >= 70) return "text-red-500";
  if (score >= 40) return "text-yellow-400";
  return "text-green-500";
};


    return (
        <div className="grid col-span-3 grid-cols-1 md:grid-cols-3 gap-6 auto-rows-min">
            
            {/* PRODUCT SECTION */}
            <aside
                onMouseEnter={() => {setProduct(true)}} 
                onMouseLeave={() => {setProduct(false)}} 
                className={`
                    bg-white rounded-2xl p-6
                    shadow transition-all duration-300 ease-in-out
                    transform border border-slate-100
                    ${product ? 'col-span-2 scale-[1.01] shadow-xl z-10' : 'col-span-1 scale-100'} 
                    ${competitors ? 'hidden' : ''}`}
            >
                <div className="flex items-center justify-between mb-6">
                    <div>
                        <h2 className="text-xl font-bold text-slate-800 capitalize">{summaryReport.product_name}</h2>
                        <span className="text-sm text-slate-500 font-medium">{summaryReport.market_position}</span>
                    </div>
                    <div className="text-right">
                        <div className={`text-2xl font-bold ${
                        getRiskColor(
                            summaryReport.overall_product_risk === "High"
                            ? 80
                            : summaryReport.overall_product_risk === "Medium"
                            ? 55
                            : 25
                        )
                        }`}>
                        {summaryReport.overall_product_risk}
                    </div>

                         <div className="text-xs text-slate-500 uppercase tracking-wide">Risk Score</div>
                    </div>
                </div>

                <div className="space-y-4">
                    <InfoItem label="Sales Outlook" value={summaryReport.monthly_sales_outlook || "N/A"} />
<InfoItem label="Market Position" value={summaryReport.market_position || "N/A"} />

                    
                    {/* Progress Bars for Scores */}
                    <div className="pt-2">
                        <div className="flex justify-between text-xs mb-1">
                            <span className="text-slate-500">Market Opportunity</span>
                            <span className="font-medium">{detailedReport.risk_and_sales_monitoring.market_opportunity_score}%</span>
                        </div>
                        <div className="h-2 w-full bg-slate-100 rounded-full overflow-hidden">
                            <div 
                                className="h-full bg-blue-500 rounded-full transition-all duration-500" 
                                style={{ width: `${detailedReport.risk_and_sales_monitoring.market_opportunity_score}%`}}
                            />
                        </div>
                    </div>
                </div>

                {product && (
                <div className="mt-8 pt-6 border-t border-slate-100 space-y-4 animate-in fade-in duration-300">
                    <h3 className="font-semibold text-slate-800 mb-2">Detailed Risk Assessment</h3>
                    <div className="grid grid-cols-2 gap-4">
                        {/* <InfoItem label="Pricing Pressure" value={detailedReport.risk_and_sales_monitoring.risk_assessment.pricing_pressure} />
                        <InfoItem label="Competitive Threat" value={detailedReport.risk_and_sales_monitoring.risk_assessment.competitive_threat} /> */}
                        <InfoItem label="Trend Direction" value={riskMonitoring.trend_direction || "N/A"} />
                        <InfoItem label="Growth Signal" value={detailedReport.risk_and_sales_monitoring.growth_signal_strength} />
                    </div>
                </div>
                )}
            </aside>

            {/* KEY METRICS CARDS */}
            <div className={`flex flex-col gap-4 ${product || competitors ? 'hidden md:flex' : ''}`}>
                 <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-100 flex-1">
                     <h3 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-3">Strongest USP</h3>
                     <p className="text-sm font-medium text-slate-800 leading-relaxed">{summaryReport.strongest_usp}</p>
                 </div>
                 <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-100 flex-1">
                     <h3 className="text-xs font-semibold text-red-400 uppercase tracking-wider mb-3">Biggest Risk</h3>
                     <p className="text-sm font-medium text-slate-800 leading-relaxed">{summaryReport.biggest_risk_factor}</p>
                 </div>
            </div>

            {/* COMPETITORS SECTION */}
            <aside
                onMouseEnter={() => {setCompetitors(true)}} 
                onMouseLeave={() => {setCompetitors(false)}}
                className={`
                    bg-white rounded-2xl p-6
                    shadow transition-all duration-300 ease-in-out
                    transform border border-slate-100
                    ${product ? 'hidden' : ''}
                    ${competitors 
                    ? 'col-span-2 scale-[1.01] shadow-xl z-10' 
                    : 'col-span-1 scale-100'
                    }
                `}
            >
                <h3 className="text-lg font-bold text-slate-800 mb-4">Competitors</h3>
                
                <div className="space-y-4">
                    {competitorsList.map((comp, idx) => (
  <div key={idx} className="group">
    <div className="flex justify-between items-center mb-1">
      <span className="font-medium text-slate-700 capitalize">
        {comp.product_name}
      </span>
      <span className="text-xs font-bold text-slate-500">
        {comp.estimated_market_share}
      </span>
    </div>
    <div className="flex justify-between text-xs text-slate-500">
      <span>{comp.company}</span>
      <span className="px-2 py-0.5 rounded-full bg-slate-100 text-slate-600">
        {comp.approval_status}
      </span>
    </div>
  </div>
))}

                </div>

                {competitors && (
  <div className="mt-6 text-sm text-slate-500">
    No detailed comparator analysis available.
  </div>
)}

            </aside>

            {/* STRATEGY & CHARTS GRID */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 col-span-1 md:col-span-3">
                <div className="space-y-4">
  <p className="text-sm text-slate-600 leading-relaxed">
    {launchStrategyText}
  </p>
</div>


                <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-100">
                    <div className="flex items-center gap-3 mb-4">
                        <div className="p-2 bg-purple-50 text-purple-600 rounded-lg">
                            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" /></svg>
                        </div>
                        <h3 className="font-bold text-slate-800">Defensive Moves</h3>
                    </div>
                    <ul className="space-y-3">
                        {marketStrategyMoves.map((move, i) => (
                            <li key={i} className="flex gap-3 text-sm text-slate-600">
                                <span className="text-purple-500 mt-0.5">•</span>
                                {move}
                            </li>
                        ))}
                    </ul>
                     <div className="mt-4 pt-4 border-t border-slate-100">
                         {strategyRecommendation.pricing_adjustment && (
  <div className="mt-4 pt-4 border-t border-slate-100">
    <InfoItem
      label="Pricing Adjustment"
      value={strategyRecommendation.pricing_adjustment}
    />
  </div>
)}

                     </div>
                </div>
            </div>

            {/* EXECUTIVE SUMMARY */}
            <div className="col-span-1 md:col-span-3 bg-gradient-to-r from-slate-900 to-slate-800 rounded-2xl p-6 shadow-lg text-white">
                <h3 className="font-bold text-white/90 mb-2 uppercase tracking-wide text-xs">Executive Summary</h3>
                <p className="text-lg font-light leading-relaxed text-slate-100 max-w-4xl">
                    {summaryReport.executive_summary}
                </p>
            </div>

        </div>
    );
}

const InfoItem = ({ label, value }) => (
    <div className="flex justify-between items-center text-sm">
        <span className="text-slate-500">{label}</span>
        <span className="font-medium text-slate-800">{value}</span>
    </div>
);

const StrategyItem = ({ label, value }) => (
  <div>
    <span className="text-xs font-bold text-slate-400 uppercase tracking-wide block mb-1">
      {label}
    </span>
    <p className="text-sm text-slate-600 leading-relaxed">
      {value}
    </p>
  </div>
);
