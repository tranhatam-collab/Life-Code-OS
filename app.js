window.LIFE_CODE_APP = {
  name: 'Life Code OS',
  domain: 'lifecode.iai.one',
  version: '1.0.0',
  environment: 'production',
  apiBase: 'https://life-code-api.tranhatam.workers.dev',
  projectStatus: {
    foundationLocked: true,
    lifeCodeIndexV1: true,
    timelineAlgorithm: true,
    riskWealthMissionFormulas: true,
    fullReportEngine: false,
    webAppIntegration: true
  },
  levels: [
    {
      code: 'level1',
      name: 'Self Signal',
      report: 'Level1_SelfSignal_Report',
      pages: '30-50'
    },
    {
      code: 'level2',
      name: 'Inner Architecture',
      report: 'Level2_InnerArchitecture_Report',
      pages: '40-60'
    },
    {
      code: 'level3',
      name: 'Behavior Code',
      report: 'Level3_BehaviorCode_Report',
      pages: '50-70'
    },
    {
      code: 'level4',
      name: 'Work & Wealth Code',
      report: 'Level4_WealthCode_Report',
      pages: '50-80'
    },
    {
      code: 'level5',
      name: 'Relationship Field',
      report: 'Level5_RelationshipField_Report',
      pages: '50-80'
    },
    {
      code: 'level6',
      name: 'Life Timeline',
      report: 'Level6_LifeTimeline_Report',
      pages: '60-100'
    },
    {
      code: 'level7',
      name: 'Body Intelligence',
      report: 'Level7_BodyIntelligence_Report',
      pages: '60-120'
    },
    {
      code: 'level8',
      name: 'Mission Path',
      report: 'Level8_MissionPath_Report',
      pages: '80-150'
    },
    {
      code: 'level9',
      name: 'Full Life Code',
      report: 'Level9_FullLifeCodeBook',
      pages: '150-600'
    }
  ],
  stepOne: {
    formulas: [
      'raw_lci',
      'normalized_lci',
      'adjusted_lci',
      'data_coverage'
    ],
    outputStatus: [
      'insufficient',
      'partial',
      'strong',
      'full'
    ]
  },
  coverageRules: {
    insufficient: { max: 0.25, label: 'Dữ liệu chưa đủ' },
    partial: { max: 0.55, label: 'Dữ liệu một phần' },
    strong: { max: 0.8, label: 'Dữ liệu mạnh' },
    full: { max: Infinity, label: 'Dữ liệu đầy đủ' }
  }
};
