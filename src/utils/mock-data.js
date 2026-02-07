const mockInsights = {
  title: "Key Insights",
  metrics: [
    { label: "Total Revenue", value: "$124.5K", change: "+12.3%" },
    { label: "Active Users", value: "8,432", change: "+5.7%" },
    { label: "Conversion Rate", value: "3.2%", change: "+0.8%" }
  ]
};

const mockInfo = {
  title: "Quick Info",
  items: [
    { label: "Last Updated", value: "2 hours ago" },
    { label: "Data Quality", value: "98.5%" },
    { label: "Sources", value: "12 active" }
  ]
};

const mockChartData = {
  title: "Performance Overview",
  description: "Monthly trends and analytics",
  data: [
    { month: "Jan", value: 65 },
    { month: "Feb", value: 72 },
    { month: "Mar", value: 68 },
    { month: "Apr", value: 85 },
    { month: "May", value: 92 },
    { month: "Jun", value: 88 }
  ]
};

const mockSnippets = [
  {
    id: 1,
    title: "Q4 Performance Report",
    description: "Quarterly results show strong growth across all segments",
    timestamp: "2 hours ago",
    tag: "Report"
  },
  {
    id: 2,
    title: "Customer Feedback Summary",
    description: "Net Promoter Score increased to 72, up from 68 last quarter",
    timestamp: "5 hours ago",
    tag: "Analysis"
  },
  {
    id: 3,
    title: "Market Trends Update",
    description: "Emerging opportunities in the APAC region identified",
    timestamp: "1 day ago",
    tag: "Insight"
  },
  {
    id: 4,
    title: "Tech Stack Review",
    description: "Recommendations for infrastructure optimization",
    timestamp: "2 days ago",
    tag: "Technical"
  }
];

const mockNews = [
  {
    id: 1,
    title: "Industry Report: AI Adoption Accelerates",
    source: "Tech Daily",
    timestamp: "1 hour ago",
    category: "Technology"
  },
  {
    id: 2,
    title: "Market Analysis: Q1 Projections",
    source: "Financial Times",
    timestamp: "3 hours ago",
    category: "Finance"
  },
  {
    id: 3,
    title: "New Regulations Impact SaaS Sector",
    source: "Business Wire",
    timestamp: "5 hours ago",
    category: "Regulatory"
  },
  {
    id: 4,
    title: "Customer Experience Trends 2026",
    source: "CX Magazine",
    timestamp: "8 hours ago",
    category: "Business"
  },
  {
    id: 5,
    title: "Cloud Infrastructure Innovations",
    source: "Cloud News",
    timestamp: "12 hours ago",
    category: "Technology"
  }
];

export const market_intelligence = {
    scout_output: {
      events: [
        {
          event_id: 1,
          title: "Fierce Pharma Biopharma News & Insights",
          companies: ["Drug companies"],
          therapy_area: "General pharma industry news",
          event_type: "News | Analysis",
          summary: "Breaking news and analysis about drug companies, the FDA, manufacturing.",
          strategic_impact: "Provides insights into current trends affecting multiple aspects of the pharma industry including regulatory changes and market dynamics.",
          importance_score: 9
        },
        {
          event_id: 2,
          title: "Regulatory Update: EMA Guidelines on AI in Clinical Trials",
          companies: ["European Medicines Agency", "All Pharma"],
          therapy_area: "Regulatory / R&D",
          event_type: "Regulation Update",
          summary: "New guidelines released by EMA regarding the use of AI/ML in clinical trial data analysis, emphasizing transparency and validation.",
          strategic_impact: "Requires updates to standard operating procedures for clinical data management; opportunity to lead in AI-compliant trials.",
          importance_score: 8
        },
        {
          event_id: 3,
          title: "Competitor Alert: Vertex Announces Positive Phase 3 Results",
          companies: ["Vertex Pharmaceuticals"],
          therapy_area: "Pain Management",
          event_type: "Clinical Trial Results",
          summary: "Vertex announces positive Phase 3 results for non-opioid painkiller, potential blockbuster rival.",
          strategic_impact: "High competitive threat to our pain management portfolio; necessitates review of marketing claims and differentiation strategy.",
          importance_score: 10
        }
      ]
    },
    signal_analysis: {
      signals: [
        {
          event_id: 1,
          event_title: "Fierce Pharma Biopharma News & Insights",
          category: "Competitive Threat | Market Opportunity | Regulatory Risk",
          impact_score: 9,
          confidence_score: 10,
          reason: "The event provides insights into current trends affecting multiple aspects of the pharma industry including regulatory changes and market dynamics which can pose competitive threats or present new opportunities."
        },
        {
          event_id: 2,
          event_title: "EMA Guidelines on AI",
          category: "Regulatory Risk | Operational Change",
          impact_score: 8,
          confidence_score: 9,
          reason: "Direct impact on R&D operations and compliance requirements for European trials."
        },
        {
          event_id: 3,
          event_title: "Vertex Phase 3 Success",
          category: "Competitive Threat",
          impact_score: 10,
          confidence_score: 10,
          reason: "Imminent market entry of a strong competitor in our core therapy area."
        }
      ]
    },
    strategic_insights: {
      market_trend: "Increasing demand for personalized medicine",
      threat_level: "High",
      opportunity_areas: ["Personalized Medicine Development"],
      competitive_pressure_score: 8,
      recommended_moves: [
        "Increase R&D investment in personalized medicine.",
        "Form strategic alliances with biotech firms specializing in genomics."
      ],
      strategic_summary: "The pharmaceutical industry faces high competitive pressure due to regulatory changes and market dynamics. Personalized medicine development presents a significant opportunity, warranting increased R&D investment and strategic alliances with biotech firms."
    },
    market_supervisor_summary: {
      overall_market_condition: "Increasing demand for personalized medicine",
      top_priority: "Personalized Medicine Development",
      risk_index: 9,
      capital_allocation_focus: ["R&D investment in personalized medicine"],
      immediate_actions: [
        "Increase R&D investment in personalized medicine.",
        "Form strategic alliances with biotech firms specializing in genomics."
      ],
      executive_summary: "The pharmaceutical industry is at a pivotal point where the high demand for personalized medicine, coupled with significant competitive pressure and regulatory changes, necessitates immediate action. By prioritizing investment in R&D focused on this area and forming strategic alliances with biotech firms specializing in genomics, we can capitalize on emerging opportunities while mitigating risks."
    }
  }

// Product Intelligence Core
export const productIntelligence = [{
  target_product: "metamorphin",

  product_scout: {
    similar_products: [
      {
        product_name: "pharmatinex",
        company: "HealFast Pharmaceuticals Inc.",
        therapy_area: "Pain Management",
        approval_status: "Approved",
        estimated_market_share: "20%",
        pricing_position: "Competitive"
      },
      {
        product_name: "reliefpro",
        company: "CureAll Pharmaceuticals Ltd.",
        therapy_area: "Pain Management",
        approval_status: "Phase III",
        estimated_market_share: "15%",
        pricing_position: "Low Cost"
      }
    ]
  },

  risk_and_sales_monitoring: {
    risk_assessment: {
      regulatory_risk: "Medium",
      pricing_pressure: "High",
      competitive_threat: "High"
    },
    sales_momentum: {
      trend_direction: "Declining",
      growth_signal_strength: "Weak"
    },
    market_opportunity_score: 40,
    overall_risk_score: 30
  },

  usp_analysis: {
    comparators: [
      {
        product_name: "pharmatinex",
        unique_selling_points: ["Approved status in the market"],
        why_sales_are_strong:
          "Estimated Market Share of 20% due to its Approval Status.",
        innovation_factor: null
      },
      {
        product_name: "reliefpro",
        unique_selling_points: ["Phase III approval status"],
        why_sales_are_strong:
          "Estimated Market Share of 15% due to its Phase III Approval Status and Low Cost pricing.",
        innovation_factor: null
      }
    ]
  },

  strategy_recommendation: {
    new_product_launch_strategy: {
      pricing_strategy:
        "Competitive pricing based on cost-plus margin to ensure affordability while maintaining profit margins.",
      positioning_strategy:
        "Position as a leading innovative treatment option in the market, highlighting clinical trial success and FDA approval status for new products.",
      target_segment:
        "Prioritize target segments with unmet medical needs where the product's unique selling points can provide significant value over competitors.",
      partnership_recommendation:
        "Form strategic alliances with healthcare providers and patient advocacy groups to enhance credibility and access."
    },

    existing_product_market_strategy: {
      defensive_moves: [
        "Increase educational marketing efforts highlighting the safety profile of existing products.",
        "Expand patient assistance programs to improve product loyalty and mitigate price sensitivity."
      ],
      pricing_adjustment:
        "Implement a tiered pricing strategy that offers discounts for bulk purchases by healthcare providers while maintaining retail prices.",
      marketing_focus:
        "Shift marketing focus towards patient success stories and long-term treatment benefits to reinforce product value."
    }
  }
}];

// Final Executive Report
export const finalExecutiveProductIntelligenceReport = [{
    product_name: "metamorphin",
    overall_product_risk: "High",
    market_position: "Challenger",
    core_competitors: ["pharmatinex", "reliefpro"],
    monthly_sales_outlook: "Declining",
    strongest_usp:
      "Opportunity to differentiate through innovative positioning and alignment with personalized medicine trends.",
    biggest_risk_factor:
      "High pricing pressure and competitive intensity combined with weak sales momentum.",
    launch_strategy_recommendation:
      "Pursue a focused launch targeting unmet pain management segments, supported by strategic partnerships, competitive pricing, and strong clinical differentiation messaging.",
    existing_product_strategy_update:
      "Defend share through tiered pricing, expanded patient assistance programs, and education-led marketing emphasizing safety and long-term outcomes.",
    executive_summary:
      "Metamorphin operates as a challenger in a highly competitive pain management market with declining sales momentum and elevated risk. Strategic repositioning, sharper differentiation, and partnerships aligned to personalized medicine are critical to stabilizing performance and unlocking future growth."
    },
    {
      product_name: "pharmatinex",
      overall_product_risk: "High",
      market_position: "Challenger",
      core_competitors: ["metamorphin", "reliefpro"],
      monthly_sales_outlook: "Declining",
      strongest_usp:
        "Opportunity to differentiate through innovative positioning and alignment with personalized medicine trends.",
      biggest_risk_factor:
        "High pricing pressure and competitive intensity combined with weak sales momentum.",
      launch_strategy_recommendation:
        "Pursue a focused launch targeting unmet pain management segments, supported by strategic partnerships, competitive pricing, and strong clinical differentiation messaging.",
      existing_product_strategy_update:
        "Defend share through tiered pricing, expanded patient assistance programs, and education-led marketing emphasizing safety and long-term outcomes.",
      executive_summary:
        "Metamorphin operates as a challenger in a highly competitive pain management market with declining sales momentum and elevated risk. Strategic repositioning, sharper differentiation, and partnerships aligned to personalized medicine are critical to stabilizing performance and unlocking future growth."
    }];


export {mockChartData, mockInfo, mockInsights, mockNews, mockSnippets}