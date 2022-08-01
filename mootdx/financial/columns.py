columns = [
    "report_date",
    "基本每股收益",
    "扣除非经常性损益每股收益",
    "每股未分配利润",
    "每股净资产",
    "每股资本公积金",
    "净资产收益率",
    "每股经营现金流量",
    "货币资金",
    "交易性金融资产",
    "应收票据",
    "应收账款",
    "预付款项",
    "其他应收款",
    "应收关联公司款",
    "应收利息",
    "应收股利",
    "存货",
    "其中：消耗性生物资产",
    "一年内到期的非流动资产",
    "其他流动资产",
    "流动资产合计",
    "可供出售金融资产",
    "持有至到期投资",
    "长期应收款",
    "长期股权投资",
    "投资性房地产",
    "固定资产",
    "在建工程",
    "工程物资",
    "固定资产清理",
    "生产性生物资产",
    "油气资产",
    "无形资产",
    "开发支出",
    "商誉",
    "长期待摊费用",
    "递延所得税资产",
    "其他非流动资产",
    "非流动资产合计",
    "资产总计",
    "短期借款",
    "交易性金融负债",
    "应付票据",
    "应付账款",
    "预收款项",
    "应付职工薪酬",
    "应交税费",
    "应付利息",
    "应付股利",
    "其他应付款",
    "应付关联公司款",
    "一年内到期的非流动负债",
    "其他流动负债",
    "流动负债合计",
    "长期借款",
    "应付债券",
    "长期应付款",
    "专项应付款",
    "预计负债",
    "递延所得税负债",
    "其他非流动负债",
    "非流动负债合计",
    "负债合计",
    "实收资本（或股本）",
    "资本公积",
    "盈余公积",
    "减：库存股",
    "未分配利润",
    "少数股东权益",
    "外币报表折算价差",
    "非正常经营项目收益调整",
    "所有者权益（或股东权益）合计",
    "负债和所有者（或股东权益）合计",
    "其中：营业收入",
    "其中：营业成本",
    "营业税金及附加",
    "销售费用",
    "管理费用",
    "勘探费用",
    "财务费用",
    "资产减值损失",
    "加：公允价值变动净收益",
    "投资收益",
    "其中：对联营企业和合营企业的投资收益",
    "影响营业利润的其他科目",
    "三、营业利润",
    "加：补贴收入",
    "营业外收入",
    "减：营业外支出",
    "其中：非流动资产处置净损失",
    "加：影响利润总额的其他科目",
    "四、利润总额",
    "减：所得税",
    "加：影响净利润的其他科目",
    "五、净利润",
    "归属于母公司所有者的净利润",
    "少数股东损益",
    "销售商品、提供劳务收到的现金",
    "收到的税费返还",
    "收到其他与经营活动有关的现金",
    "经营活动现金流入小计",
    "购买商品、接受劳务支付的现金",
    "支付给职工以及为职工支付的现金",
    "支付的各项税费",
    "支付其他与经营活动有关的现金",
    "经营活动现金流出小计",
    "经营活动产生的现金流量净额",
    "收回投资收到的现金",
    "取得投资收益收到的现金",
    "处置固定资产、无形资产和其他长期资产收回的现金净额",
    "处置子公司及其他营业单位收到的现金净额",
    "收到其他与投资活动有关的现金",
    "投资活动现金流入小计",
    "购建固定资产、无形资产和其他长期资产支付的现金",
    "投资支付的现金",
    "取得子公司及其他营业单位支付的现金净额",
    "支付其他与投资活动有关的现金",
    "投资活动现金流出小计",
    "投资活动产生的现金流量净额",
    "吸收投资收到的现金",
    "取得借款收到的现金",
    "收到其他与筹资活动有关的现金",
    "筹资活动现金流入小计",
    "偿还债务支付的现金",
    "分配股利、利润或偿付利息支付的现金",
    "支付其他与筹资活动有关的现金",
    "筹资活动现金流出小计",
    "筹资活动产生的现金流量净额",
    "四、汇率变动对现金的影响",
    "四(2)、其他原因对现金的影响",
    "五、现金及现金等价物净增加额",
    "期初现金及现金等价物余额",
    "期末现金及现金等价物余额",
    "净利润",
    "加：资产减值准备",
    "固定资产折旧、油气资产折耗、生产性生物资产折旧",
    "无形资产摊销",
    "长期待摊费用摊销",
    "处置固定资产、无形资产和其他长期资产的损失",
    "固定资产报废损失",
    "公允价值变动损失",
    "财务费用",
    "投资损失",
    "递延所得税资产减少",
    "递延所得税负债增加",
    "存货的减少",
    "经营性应收项目的减少",
    "经营性应付项目的增加",
    "其他",
    "经营活动产生的现金流量净额2",
    "债务转为资本",
    "一年内到期的可转换公司债券",
    "融资租入固定资产",
    "现金的期末余额",
    "减：现金的期初余额",
    "加：现金等价物的期末余额",
    "减：现金等价物的期初余额",
    "现金及现金等价物净增加额",
    "流动比率(非金融类指标)",
    "速动比率(非金融类指标)",
    "现金比率(%)(非金融类指标)",
    "利息保障倍数(非金融类指标)",
    "非流动负债比率(%)(非金融类指标)",
    "流动负债比率(%)(非金融类指标)",
    "现金到期债务比率(%)(非金融类指标)",
    "有形资产净值债务率(%)",
    "权益乘数(%)",
    "股东的权益/负债合计(%)",
    "有形资产/负债合计(%)",
    "经营活动产生的现金流量净额/负债合计(%)(非金融类指标)",
    "EBITDA/负债合计(%)(非金融类指标)",
    "应收帐款周转率(非金融类指标)",
    "存货周转率(非金融类指标)",
    "运营资金周转率(非金融类指标)",
    "总资产周转率(非金融类指标)",
    "固定资产周转率(非金融类指标)",
    "应收帐款周转天数(非金融类指标)",
    "存货周转天数(非金融类指标)",
    "流动资产周转率(非金融类指标)",
    "流动资产周转天数(非金融类指标)",
    "总资产周转天数(非金融类指标)",
    "股东权益周转率(非金融类指标)",
    "营业收入增长率(%)",
    "净利润增长率(%)",
    "净资产增长率(%)",
    "固定资产增长率(%)",
    "总资产增长率(%)",
    "投资收益增长率(%)",
    "营业利润增长率(%)",
    "扣非每股收益同比(%)",
    "扣非净利润同比(%)",
    "暂无",
    "成本费用利润率(%)",
    "营业利润率(非金融类指标)",
    "营业税金率(非金融类指标)",
    "营业成本率(非金融类指标)",
    "净资产收益率",
    "投资收益率",
    "销售净利率(%)",
    "总资产报酬率",
    "净利润率(非金融类指标)",
    "销售毛利率(%)(非金融类指标)",
    "三费比重(非金融类指标)",
    "管理费用率(非金融类指标)",
    "财务费用率(非金融类指标)",
    "扣除非经常性损益后的净利润",
    "息税前利润(EBIT)",
    "息税折旧摊销前利润(EBITDA)",
    "EBITDA/营业总收入(%)(非金融类指标)",
    "资产负债率(%)",
    "流动资产比率(非金融类指标)",
    "货币资金比率(非金融类指标)",
    "存货比率(非金融类指标)",
    "固定资产比率",
    "负债结构比(非金融类指标)",
    "归属于母公司股东权益/全部投入资本(%)",
    "股东的权益/带息债务(%)",
    "有形资产/净债务(%)",
    "每股经营性现金流(元)",
    "营业收入现金含量(%)(非金融类指标)",
    "经营活动产生的现金流量净额/经营活动净收益(%)",
    "销售商品提供劳务收到的现金/营业收入(%)",
    "经营活动产生的现金流量净额/营业收入",
    "资本支出/折旧和摊销",
    "每股现金流量净额(元)",
    "经营净现金比率（短期债务）(非金融类指标)",
    "经营净现金比率（全部债务）",
    "经营活动现金净流量与净利润比率",
    "全部资产现金回收率",
    "营业收入",
    "营业利润",
    "归属于母公司所有者的净利润",
    "扣除非经常性损益后的净利润",
    "经营活动产生的现金流量净额",
    "投资活动产生的现金流量净额",
    "筹资活动产生的现金流量净额",
    "现金及现金等价物净增加额",
    "总股本",
    "已上市流通A股",
    "已上市流通B股",
    "已上市流通H股",
    "股东人数(户)",
    "第一大股东的持股数量",
    "十大流通股东持股数量合计(股)",
    "十大股东持股数量合计(股)",
    "机构总量（家）",
    "机构持股总量(股)",
    "QFII机构数",
    "QFII持股量",
    "券商机构数",
    "券商持股量",
    "保险机构数",
    "保险持股量",
    "基金机构数",
    "基金持股量",
    "社保机构数",
    "社保持股量",
    "私募机构数",
    "私募持股量",
    "财务公司机构数",
    "财务公司持股量",
    "年金机构数",
    "年金持股量",
    "十大流通股东中持有A股合计(股)",
    "第一大流通股东持股量(股)",
    "自由流通股(股)",
    "受限流通A股(股)",
    "一般风险准备(金融类)",
    "其他综合收益(利润表)",
    "综合收益总额(利润表)",
    "归属于母公司股东权益(资产负债表)",
    "银行机构数(家)(机构持股)",
    "银行持股量(股)(机构持股)",
    "一般法人机构数(家)(机构持股)",
    "一般法人持股量(股)(机构持股)",
    "近一年净利润(元)",
    "信托机构数(家)(机构持股)",
    "信托持股量(股)(机构持股)",
    "特殊法人机构数(家)(机构持股)",
    "特殊法人持股量(股)(机构持股)",
    "加权净资产收益率(每股指标)",
    "扣非每股收益(单季度财务指标)",
    "最近一年营业收入（万元）",
    "国家队持股数量（万股)",
    "业绩预告-本期净利润同比增幅下限%",
    "业绩预告-本期净利润同比增幅上限%",
    "归母净利润（业绩快报）",
    "扣非净利润（业绩快报）",
    "总资产（业绩快报）",
    "净资产（业绩快报）",
    "每股收益（业绩快报）",
    "摊薄净资产收益率（业绩快报）",
    "加权净资产收益率（业绩快报）",
    "每股净资产（业绩快报）",
    "应付票据及应付账款(资产负债表)",
    "应收票据及应收账款(资产负债表)",
    "递延收益(资产负债表)",
    "其他综合收益(资产负债表)",
    "其他权益工具(资产负债表)",
    "其他收益(利润表)",
    "资产处置收益(利润表)",
    "持续经营净利润(利润表)",
    "终止经营净利润(利润表)",
    "研发费用(利润表)",
    "其中:利息费用(利润表-财务费用)",
    "其中:利息收入(利润表-财务费用)",
    "近一年经营活动现金流净额",
    "近一年归母净利润（万元）",
    "近一年扣非净利润（万元）",
    "近一年现金净流量（万元）",
    "基本每股收益（单季度）",
    "营业总收入(单季度)(万元)",
    "业绩预告公告日期 ",
    "财报公告日期",
    "业绩快报公告日期",
    "近一年投资活动现金流净额(万元)",
    "业绩预告-本期净利润下限(万元)",
    "业绩预告-本期净利润上限(万元)",
    "营业总收入TTM(万元)",
    "员工总数(人)",
    "每股企业自由现金流",
    "每股股东自由现金流",
    "col323",
    "col324",
    "col325",
    "col326",
    "col327",
    "col328",
    "col329",
    "col330",
    "col331",
    "col332",
    "col333",
    "col334",
    "col335",
    "col336",
    "col337",
    "col338",
    "col339",
    "col340",
    "col341",
    "col342",
    "col343",
    "col344",
    "col345",
    "col346",
    "col347",
    "col348",
    "col349",
    "col350",
    "col351",
    "col352",
    "col353",
    "col354",
    "col355",
    "col356",
    "col357",
    "col358",
    "col359",
    "col360",
    "col361",
    "col362",
    "col363",
    "col364",
    "col365",
    "col366",
    "col367",
    "col368",
    "col369",
    "col370",
    "col371",
    "col372",
    "col373",
    "col374",
    "col375",
    "col376",
    "col377",
    "col378",
    "col379",
    "col380",
    "col381",
    "col382",
    "col383",
    "col384",
    "col385",
    "col386",
    "col387",
    "col388",
    "col389",
    "col390",
    "col391",
    "col392",
    "col393",
    "col394",
    "col395",
    "col396",
    "col397",
    "col398",
    "col399",
    "col400",
    "专项储备(万元)",
    "结算备付金(万元)",
    "拆出资金(万元)",
    "发放贷款及垫款(万元)(流动资产科目)",
    "衍生金融资产(万元)",
    "应收保费(万元)",
    "应收分保账款(万元)",
    "应收分保合同准备金(万元)",
    "买入返售金融资产(万元)",
    "划分为持有待售的资产(万元)",
    "发放贷款及垫款(万元)(非流动资产科目)",
    "向中央银行借款(万元)",
    "吸收存款及同业存放(万元)",
    "拆入资金(万元)",
    "衍生金融负债(万元)",
    "卖出回购金融资产款(万元)",
    "应付手续费及佣金(万元)",
    "应付分保账款(万元)",
    "保险合同准备金(万元)",
    "代理买卖证券款(万元)",
    "代理承销证券款(万元)",
    "划分为持有待售的负债(万元)",
    "预计负债(万元)",
    "递延收益(万元)（流动负债科目）",
    "其中:优先股(万元)(非流动负债科目)",
    "永续债(万元)(非流动负债科目)",
    "长期应付职工薪酬(万元)",
    "其中:优先股(万元)(所有者权益科目)",
    "永续债(万元)(所有者权益科目)",
    "债权投资(万元)",
    "其他债权投资(万元)",
    "其他权益工具投资(万元)",
    "其他非流动金融资产(万元)",
    "合同负债(万元)",
    "合同资产(万元)",
    "其他资产(万元)",
    "应收款项融资(万元)",
    "使用权资产(万元)",
    "租赁负债(万元)",
    "col440",
    "col441",
    "col442",
    "col443",
    "col444",
    "col445",
    "col446",
    "col447",
    "col448",
    "col449",
    "col450",
    "col451",
    "col452",
    "col453",
    "col454",
    "col455",
    "col456",
    "col457",
    "col458",
    "col459",
    "col460",
    "col461",
    "col462",
    "col463",
    "col464",
    "col465",
    "col466",
    "col467",
    "col468",
    "col469",
    "col470",
    "col471",
    "col472",
    "col473",
    "col474",
    "col475",
    "col476",
    "col477",
    "col478",
    "col479",
    "col480",
    "col481",
    "col482",
    "col483",
    "col484",
    "col485",
    "col486",
    "col487",
    "col488",
    "col489",
    "col490",
    "col491",
    "col492",
    "col493",
    "col494",
    "col495",
    "col496",
    "col497",
    "col498",
    "col499",
    "col500",
    "稀释每股收益(元)",
    "营业总收入(万元)",
    "汇兑收益(万元)",
    "其中:归属于母公司综合收益(万元)",
    "其中:归属于少数股东综合收益(万元)",
    "利息收入(万元)",
    "已赚保费(万元)",
    "手续费及佣金收入(万元)",
    "利息支出(万元)",
    "手续费及佣金支出(万元)",
    "退保金(万元)",
    "赔付支出净额(万元)",
    "提取保险合同准备金净额(万元)",
    "保单红利支出(万元)",
    "分保费用(万元)",
    "其中:非流动资产处置利得(万元)",
    "信用减值损失(万元)",
    "净敞口套期收益(万元)",
    "营业总成本(万元)",
    "信用减值损失(万元、2019格式)",
    "资产减值损失(万元、2019格式)",
    "col522",
    "col523",
    "col524",
    "col525",
    "col526",
    "col527",
    "col528",
    "col529",
    "col530",
    "col531",
    "col532",
    "col533",
    "col534",
    "col535",
    "col536",
    "col537",
    "col538",
    "col539",
    "col540",
    "col541",
    "col542",
    "col543",
    "col544",
    "col545",
    "col546",
    "col547",
    "col548",
    "col549",
    "col550",
    "col551",
    "col552",
    "col553",
    "col554",
    "col555",
    "col556",
    "col557",
    "col558",
    "col559",
    "col560",
    "加:其他原因对现金的影响2(万元)(现金的期末余额科目)",
    "客户存款和同业存放款项净增加额(万元)",
    "向中央银行借款净增加额(万元)",
    "向其他金融机构拆入资金净增加额(万元)",
    "收到原保险合同保费取得的现金(万元)",
    "收到再保险业务现金净额(万元)",
    "保户储金及投资款净增加额(万元)",
    "处置以公允价值计量且其变动计入当期损益的金融资产净增加额(万元)",
    "收取利息、手续费及佣金的现金(万元)",
    "拆入资金净增加额(万元)",
    "回购业务资金净增加额(万元)",
    "客户贷款及垫款净增加额(万元)",
    "存放中央银行和同业款项净增加额(万元)",
    "支付原保险合同赔付款项的现金(万元)",
    "支付利息、手续费及佣金的现金(万元)",
    "支付保单红利的现金(万元)",
    "其中:子公司吸收少数股东投资收到的现金(万元)",
    "其中:子公司支付给少数股东的股利、利润(万元)",
    "投资性房地产的折旧及摊销(万元)",
    "信用减值损失(万元)",
]
