import { ChevronLeft, Newspaper, TrendingUp, AlertTriangle, Target, Activity, ArrowRight } from "lucide-react";
import { market_intelligence } from "../utils/mock-data";

export default function NewsSection ({ isExpanded, onExpand, onCollapse }) {
  const { scout_output, signal_analysis, strategic_insights, market_supervisor_summary } = market_intelligence;
  const news = scout_output.events;

  if (isExpanded) {
    return (
      <div className="bg-slate-50 min-h-full">
        {/* Header */}
        <div className="bg-white border-b border-gray-200 sticky top-0 z-10 px-6 py-4 flex items-center gap-4 shadow-sm">
          <button
            onClick={onCollapse}
            className="p-2 hover:bg-slate-100 rounded-full transition-colors text-slate-500 hover:text-slate-800"
          >
            <ChevronLeft size={24} />
          </button>
          <div>
            <h2 className="text-xl font-bold text-slate-800 flex items-center gap-2">
              Market Intelligence Hub
              <span className="px-2 py-0.5 rounded-full bg-blue-100 text-blue-700 text-xs font-bold uppercase tracking-wide">
                Live
              </span>
            </h2>
            <p className="text-sm text-slate-500">Real-time market signals and strategic supervision</p>
          </div>
        </div>

        <div className="p-6 max-w-7xl mx-auto space-y-6">
            
            {/* Top Metrics Row */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <MetricCard 
                    label="Market Trend" 
                    value={strategic_insights.market_trend} 
                    icon={<TrendingUp size={18} />}
                    color="blue"
                />
                <MetricCard 
                    label="Threat Level" 
                    value={strategic_insights.threat_level} 
                    icon={<AlertTriangle size={18} />}
                    color={strategic_insights.threat_level === 'High' ? 'red' : 'yellow'}
                />
                <MetricCard 
                    label="Risk Index" 
                    value={`${market_supervisor_summary.risk_index}/10`} 
                    icon={<Activity size={18} />}
                    color="orange"
                    footer={
                        <div className="w-full bg-slate-200 h-1.5 rounded-full mt-2 overflow-hidden">
                            <div className="h-full bg-orange-500 rounded-full" style={{ width: `${market_supervisor_summary.risk_index * 10}%` }}></div>
                        </div>
                    }
                />
                <MetricCard 
                    label="Comp. Pressure" 
                    value={`${strategic_insights.competitive_pressure_score}/10`} 
                    icon={<Target size={18} />}
                    color="purple"
                    footer={
                        <div className="w-full bg-slate-200 h-1.5 rounded-full mt-2 overflow-hidden">
                            <div className="h-full bg-purple-500 rounded-full" style={{ width: `${strategic_insights.competitive_pressure_score * 10}%` }}></div>
                        </div>
                    }
                />
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                
                {/* Left Column: Strategic Overview */}
                <div className="lg:col-span-2 space-y-6">
                    {/* Executive Summary */}
                    <SectionCard title="Market Supervisor Executive Summary" className="bg-gradient-to-br from-slate-900 to-slate-800 text-white border-none shadow-lg">
                         <p className="text-slate-100 leading-relaxed font-light text-lg">
                            {market_supervisor_summary.executive_summary}
                         </p>
                         <div className="mt-6 flex flex-wrap gap-3">
                             {market_supervisor_summary.immediate_actions.map((action, i) => (
                                 <div key={i} className="bg-white/10 backdrop-blur-sm border border-white/10 px-3 py-2 rounded-lg text-sm text-slate-200 flex items-center gap-2">
                                     <div className="w-2 h-2 rounded-full bg-emerald-400"></div>
                                     {action}
                                 </div>
                             ))}
                         </div>
                    </SectionCard>

                    {/* Signal Analysis */}
                     <SectionCard title="Signal Analysis & Interpretation">
                        <div className="space-y-4">
                            {signal_analysis.signals.map((signal, idx) => (
                                <div key={idx} className="bg-slate-50 rounded-xl p-4 border border-slate-100 hover:border-blue-200 transition-colors">
                                    <div className="flex justify-between items-start mb-2">
                                        <h4 className="font-semibold text-slate-800">{signal.event_title}</h4>
                                        <span className="px-2 py-1 bg-blue-100 text-blue-700 text-xs font-bold rounded">
                                            Confidence: {signal.confidence_score}/10
                                        </span>
                                    </div>
                                    <p className="text-sm text-slate-600 mb-3">{signal.reason}</p>
                                    <div className="flex flex-wrap gap-2">
                                        {signal.category.split('|').map((cat, i) => (
                                            <span key={i} className="text-xs text-slate-500 bg-white border border-slate-200 px-2 py-1 rounded shadow-sm">
                                                {cat.trim()}
                                            </span>
                                        ))}
                                    </div>
                                </div>
                            ))}
                        </div>
                     </SectionCard>

                     <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                         <SectionCard title="Strategic Opportunities">
                             <ul className="space-y-3">
                                 {strategic_insights.opportunity_areas.map((opp, i) => (
                                     <li key={i} className="flex gap-3 items-start">
                                         <span className="bg-emerald-100 text-emerald-600 p-1 rounded mt-0.5">
                                             <TrendingUp size={14} />
                                         </span>
                                         <span className="text-sm text-slate-700 font-medium">{opp}</span>
                                     </li>
                                 ))}
                             </ul>
                         </SectionCard>
                         <SectionCard title="Recommended Moves" className="bg-blue-50/50 border-blue-100">
                             <ul className="space-y-3">
                                 {strategic_insights.recommended_moves.map((move, i) => (
                                     <li key={i} className="flex gap-3 items-start">
                                         <span className="text-blue-500 mt-1">•</span>
                                         <span className="text-sm text-slate-700">{move}</span>
                                     </li>
                                 ))}
                             </ul>
                         </SectionCard>
                     </div>
                </div>

                {/* Right Column: News Feed */}
                <div className="lg:col-span-1">
                    <div className="bg-white rounded-xl border border-gray-200 shadow-sm sticky top-24">
                        <div className="p-4 border-b border-gray-200 flex justify-between items-center">
                            <h3 className="font-bold text-slate-800">Raw News Feed</h3>
                            <span className="text-xs font-medium text-slate-400">{news.length} events</span>
                        </div>
                        <div className="max-h-[calc(100vh-200px)] overflow-y-auto p-2 space-y-2">
                            {news.map((item) => (
                                <div 
                                    key={item.event_id}
                                    className="p-3 hover:bg-slate-50 rounded-lg group transition-colors cursor-pointer border border-transparent hover:border-slate-100"
                                >
                                    <h4 className="text-sm font-semibold text-slate-800 mb-1 leading-snug group-hover:text-blue-600 transition-colors">
                                        {item.title}
                                    </h4>
                                    <p className="text-xs text-slate-500 line-clamp-2 mb-2">{item.summary}</p>
                                    <div className="flex items-center justify-between">
                                        <div className="flex gap-2">
                                            {item.companies.map((c, i) => (
                                                <span key={i} className="text-[10px] text-slate-400 bg-slate-100 px-1.5 py-0.5 rounded">
                                                    {c}
                                                </span>
                                            ))}
                                        </div>
                                        <span className={`text-[10px] font-bold ${item.importance_score >= 8 ? 'text-red-500' : 'text-slate-400'}`}>
                                            Impact: {item.importance_score}
                                        </span>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>

            </div>

        </div>
      </div>
    );
  }

  // Collapsed View
  return (
    <div 
      onClick={onExpand}
      className="w-full lg:w-64 bg-white rounded-xl border border-gray-200 p-4 shadow-sm 
      hover:shadow-md hover:border-blue-300 transition-all cursor-pointer group"
    >
      <div className="flex items-center justify-between mb-4">
        <div>
            <h3 className="text-sm font-bold text-gray-900">Market Intel</h3>
            <p className="text-xs text-slate-500">{scout_output.events.length} New Signals</p>
        </div>
        <div className="relative">
            <Newspaper size={20} className="text-gray-400 group-hover:text-blue-500 transition-colors" />
            <span className="absolute -top-1 -right-1 flex h-2.5 w-2.5">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-red-400 opacity-75"></span>
                <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-red-500"></span>
            </span>
        </div>
      </div>
      
      <div className="space-y-4">
        
        {/* Mini Highlights */}
        <div className="space-y-3">
             {news.slice(0, 3).map((item) => (
               <div key={item.event_id} className="pb-3 border-b border-gray-100 last:border-0">
                 <h4 className="text-xs font-medium text-gray-900 mb-1 line-clamp-2 group-hover:text-blue-600 transition-colors">
                   {item.title}
                 </h4>
                 <div className="flex justify-between items-center">
                    <span className="text-[10px] text-gray-400">{item.therapy_area}</span>
                    <span className="text-[10px] font-semibold text-slate-500">Score: {item.importance_score}</span>
                 </div>
               </div>
             ))}
        </div>

        <button className="w-full flex items-center justify-center gap-1 text-xs font-medium text-blue-600 bg-blue-50 py-2 rounded-lg group-hover:bg-blue-100 transition-colors">
            View Analytics <ArrowRight size={12} />
        </button>
      </div>
    </div>
  );
};

// Helper Components
function MetricCard({ label, value, icon, color, footer }) {
    const colorClasses = {
        blue: "text-blue-600 bg-blue-50",
        red: "text-red-600 bg-red-50",
        orange: "text-orange-600 bg-orange-50",
        yellow: "text-yellow-600 bg-yellow-50",
        purple: "text-purple-600 bg-purple-50",
        green: "text-emerald-600 bg-emerald-50",
    };

    return (
        <div className="bg-white p-4 rounded-xl shadow-sm border border-slate-100 flex flex-col justify-between">
            <div className="flex items-start justify-between mb-2">
                <span className="text-slate-500 text-xs font-bold uppercase tracking-wider">{label}</span>
                <div className={`p-2 rounded-lg ${colorClasses[color] || colorClasses.blue}`}>
                    {icon}
                </div>
            </div>
            <div>
                <div className="text-2xl font-bold text-slate-800">{value}</div>
            </div>
            {footer}
        </div>
    );
}

function SectionCard({ title, children, className = "" }) {
    return (
        <div className={`bg-white rounded-xl border border-gray-200 shadow-sm p-6 ${className}`}>
            <h3 className="text-lg font-bold text-slate-800 mb-4">{title}</h3>
            {children}
        </div>
    );
}