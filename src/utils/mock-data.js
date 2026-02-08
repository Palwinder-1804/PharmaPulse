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
        },
        {
          event_id: 4,
          title: "Health & Pharma News | Latest Healthcare Stories",
          companies: ["Global pharmaceutical companies"],
          therapy_area: "General health and pharma news coverage",
          event_type: "News | Drug Launches, FDA Approvals, Safety Warnings",
          summary: "Latest international drug industry stories.",
          strategic_impact: "Offers a global perspective on recent healthcare and pharma developments.",
          importance_score: 7
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
    overall_risk_score: 75
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
},
{
  target_product: "paracetamol",

  product_scout: {
    similar_products: [
      {
        product_name: "Panadol Extra Strength",
        company: "McNeil Consumer Healthcare",
        therapy_area: "Pain Relief and Fever Reducer",
        approval_status: "Approved",
        estimated_market_share: "20%",
        pricing_position: "Competitive"

      },
      {

        product_name: "Tylenol 3 Extra Strength",

        company: "McNeil Consumer Healthcare",

        therapy_area: "Pain Relief and Fever Reducer",

        approval_status: "Approved",

        estimated_market_share: "15%",

        pricing_position: "Low Cost"
      }
    ]
  },

  risk_and_sales_monitoring: {
    risk_assessment: {

      regulatory_risk: "Low",

      pricing_pressure: "Medium",

      competitive_threat: "High"

    },
    sales_momentum: {

      trend_direction: "Stable",

      growth_signal_strength: "Weak"

    },
    market_opportunity_score: 60,
    overall_risk_score: 75
  },

  usp_analysis: {
    comparators: [
      {

        product_name: "Panadol Extra Strength",

        unique_selling_points: ["Stronger pain relief formulation"],

        why_sales_are_strong: "High market share due to brand recognition and established trust in efficacy.",

        innovation_factor: "Developed as a stronger, more effective version of paracetamol for severe pain."

      },

      {

        product_name: "Tylenol 3 Extra Strength",

        unique_selling_points: ["Combination with codeine"],

        why_sales_are_strong: "Low cost and dual-action pain relief make it a popular choice for budget consumers.",

        innovation_factor: "Innovative formulation that provides both analgesic and antitussive effects."

      }
    ]
  },

  strategy_recommendation: {
    new_product_launch_strategy: {

      pricing_strategy: "Penetrate the market with a competitive introductory price point below Tylenol 3 Extra Strength, leveraging its popularity and cost-effectiveness.",

      positioning_strategy: "Position as an advanced formulation offering stronger pain relief without codeine for those seeking non-opioid options or with concerns about addiction risks.",

      target_segment: "Budget-conscious consumers and individuals looking for a potent, yet safe alternative to opioids in severe pain management scenarios.",

      partnership_recommendation: "Collaborate with healthcare providers specializing in chronic pain treatment to endorse the product's efficacy and safety profile."

    },

    existing_product_market_strategy: {

      defensive_moves: ["Enhance brand loyalty programs", "Increase educational marketing on safe usage"],

      pricing_adjustment: "Maintain current pricing to preserve perceived value while ensuring affordability.",

      marketing_focus: "Highlight the product's long-standing efficacy and safety record, emphasizing its role in managing chronic pain effectively."      

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
      product_name: "tylenolplus",
      overall_product_risk: "Medium",
      market_position: "Challenger",
      core_competitors: ["tylenol extra strength"],
      monthly_sales_outlook: "Growing",
      strongest_usp: "Non-opioid pain relief with a potent formula.",
      biggest_risk_factor: "Potential market resistance to new formulations and pricing strategies.",
      launch_strategy_recommendation:
        "Adopt the proposed penetrative pricing strategy, emphasize non-opioid benefits in positioning, target budget-conscious consumers with chronic pain needs, and seek partnerships for endorsement from healthcare providers.",
      existing_product_strategy_update:
        "Maintain current pricing while enhancing brand loyalty programs to preserve perceived value. Increase educational marketing on safe usage without altering the product's efficacy and safety record narrative.",
      executive_summary:
        "Tylenol Plus is poised for growth with a strong USP of non-opioid, potent pain relief; however, faces medium risk due to potential resistance. A strategic launch focusing on affordability, targeted marketing, and healthcare partnerships will be key."
    }
  ];


