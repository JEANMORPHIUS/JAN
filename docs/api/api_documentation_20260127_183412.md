# JAN Studio API

**Version:** 1.0.0  
**Generated:** 2026-01-27T18:34:12.746029

API for JAN Studio - Markdown-based creative identity system
    
    ORGANIZATIONAL STRUCTURE:
    We are running as a .org (nonprofit organization).
    The others are our employees.
    We serve as stewards of The Table.
    
    THE MISSION (Shell - Public Language):
    We are building an educational platform that transforms lives through values-based education, 
    creating global impact through digital inclusion, honoring our mission to serve communities, 
    and trusting in the process.
    
    THE MISSION (Seed - Internal Truth):
    We are building a ministry, sharing God's message, our mission carries kingdom impact, 
    we honor the Lord's holy assignment, have faith.
    

## Table of Contents

1. [GET /api/jan/personas](#get-apijanpersonas) - Get Personas
2. [POST /api/jan/personas](#post-apijanpersonas) - Create Persona
3. [GET /api/jan/personas/{persona_name}/files](#get-apijanpersonaspersona_namefiles) - Get Persona Files
4. [GET /api/jan/personas/{persona_name}/files/{file_name}](#get-apijanpersonaspersona_namefilesfile_name) - Get Persona File
5. [PUT /api/jan/personas/{persona_name}/files/{file_name}](#put-apijanpersonaspersona_namefilesfile_name) - Save Persona File
6. [DELETE /api/jan/personas/{persona_name}](#delete-apijanpersonaspersona_name) - Delete Persona
7. [POST /api/jan/generate](#post-apijangenerate) - Generate Content
8. [GET /api/marketplace/personas](#get-apimarketplacepersonas) - Browse Personas
9. [POST /api/marketplace/personas](#post-apimarketplacepersonas) - Submit Persona
10. [GET /api/marketplace/personas/{persona_id}](#get-apimarketplacepersonaspersona_id) - Get Persona Details
11. [POST /api/marketplace/personas/{persona_id}/download](#post-apimarketplacepersonaspersona_iddownload) - Download Persona
12. [POST /api/marketplace/personas/{persona_id}/rate](#post-apimarketplacepersonaspersona_idrate) - Rate Persona
13. [GET /api/marketplace/categories](#get-apimarketplacecategories) - Get Categories
14. [POST /api/auth/register](#post-apiauthregister) - Register
15. [POST /api/auth/login](#post-apiauthlogin) - Login
16. [POST /api/auth/refresh](#post-apiauthrefresh) - Refresh Token
17. [GET /api/auth/me](#get-apiauthme) - Get Current User Info
18. [POST /api/auth/logout](#post-apiauthlogout) - Logout
19. [GET /api/auth/admin/users](#get-apiauthadminusers) - List Users
20. [PUT /api/auth/admin/users/{user_id}/status](#put-apiauthadminusersuser_idstatus) - Update User Status
21. [POST /api/oracle/cast](#post-apioraclecast) - Cast Oracle
22. [GET /api/oracle/session](#get-apioraclesession) - Get Session
23. [POST /api/oracle/break](#post-apioraclebreak) - Record Break
24. [GET /api/oracle/history](#get-apioraclehistory) - Get Cast History
25. [POST /api/oracle-matrix/audit/{system_type}](#post-apioracle-matrixauditsystem_type) - Audit System
26. [POST /api/oracle-matrix/apply/{system_type}](#post-apioracle-matrixapplysystem_type) - Apply Oracle Matrix
27. [POST /api/oracle-matrix/audit-all](#post-apioracle-matrixaudit-all) - Audit All Systems
28. [GET /api/oracle-matrix/status](#get-apioracle-matrixstatus) - Get Integration Status
29. [GET /api/oracle-matrix/systems](#get-apioracle-matrixsystems) - List Systems
30. [POST /api/oracle-matrix/apply-all](#post-apioracle-matrixapply-all) - Apply To All Systems
31. [POST /api/game-of-racon/cast](#post-apigame-of-raconcast) - Cast Spiritual Oracle
32. [POST /api/game-of-racon/homework/submit](#post-apigame-of-raconhomeworksubmit) - Submit Homework Assignment
33. [GET /api/game-of-racon/homework/pending](#get-apigame-of-raconhomeworkpending) - Get Pending Homework Assignments
34. [GET /api/game-of-racon/session](#get-apigame-of-raconsession) - Get Spiritual Session
35. [POST /api/oracle-gateway/read-cards](#post-apioracle-gatewayread-cards) - Read The Cards
36. [GET /api/oracle-gateway/check-access](#get-apioracle-gatewaycheck-access) - Check Access
37. [GET /api/oracle-gateway/visitor/{visitor_id}](#get-apioracle-gatewayvisitorvisitor_id) - Get Visitor Info
38. [GET /api/oracle-gateway/message](#get-apioracle-gatewaymessage) - Get Gateway Message
39. [POST /api/oracle-universal/cast](#post-apioracle-universalcast) - Cast Universal
40. [GET /api/oracle-universal/principle](#get-apioracle-universalprinciple) - Get Universal Principle
41. [GET /api/heritage/timeline/{dimension}](#get-apiheritagetimelinedimension) - Get Timeline Sites
42. [GET /api/heritage/chronology](#get-apiheritagechronology) - Get Chronology
43. [GET /api/heritage/patterns](#get-apiheritagepatterns) - Get Patterns
44. [GET /api/heritage/site/{site_id}](#get-apiheritagesitesite_id) - Get Site Details
45. [POST /api/heritage/site](#post-apiheritagesite) - Create Heritage Site
46. [GET /api/heritage/search](#get-apiheritagesearch) - Search Heritage
47. [GET /api/heritage/stats](#get-apiheritagestats) - Get Heritage Stats
48. [POST /api/heritage/cleanse](#post-apiheritagecleanse) - Cleanse Narrative
49. [POST /api/heritage/care-package](#post-apiheritagecare-package) - Care Package Cleanse
50. [GET /api/heritage/sanctuary/status](#get-apiheritagesanctuarystatus) - Get Sanctuary Status
51. [GET /api/heritage-meridian/status](#get-apiheritage-meridianstatus) - Get Status
52. [GET /api/heritage-meridian/pillars](#get-apiheritage-meridianpillars) - Get Pillars
53. [GET /api/heritage-meridian/pillars/{pillar_id}](#get-apiheritage-meridianpillarspillar_id) - Get Pillar
54. [GET /api/heritage-meridian/wonders](#get-apiheritage-meridianwonders) - Get Wonders
55. [GET /api/heritage-meridian/wonders/{wonder_id}](#get-apiheritage-meridianwonderswonder_id) - Get Wonder
56. [GET /api/heritage-meridian/meridians](#get-apiheritage-meridianmeridians) - Get Meridians
57. [GET /api/heritage-meridian/network-health](#get-apiheritage-meridiannetwork-health) - Get Network Health
58. [GET /api/heritage-meridian/7-wonders/list](#get-apiheritage-meridian7-wonderslist) - Get 7 Wonders List
59. [GET /api/heritage-meridian/7-wonders/{wonder_id}](#get-apiheritage-meridian7-wonderswonder_id) - Get 7 Wonder
60. [GET /api/heritage-meridian/7-wonders/{wonder_id}/resonance](#get-apiheritage-meridian7-wonderswonder_idresonance) - Get Wonder Resonance
61. [GET /api/heritage-meridian/7-wonders/{wonder_id}/meridian-connections](#get-apiheritage-meridian7-wonderswonder_idmeridian-connections) - Get Wonder Meridian Connections
62. [GET /api/health/templates](#get-apihealthtemplates) - Get Condition Templates
63. [POST /api/health/condition](#post-apihealthcondition) - Register Condition
64. [POST /api/health/log](#post-apihealthlog) - Log Health Entry
65. [GET /api/health/summary](#get-apihealthsummary) - Get Health Summary
66. [GET /api/health/export](#get-apihealthexport) - Export Health Data
67. [GET /api/health/status](#get-apihealthstatus) - Health Api Status
68. [GET /api/educational/overview](#get-apieducationaloverview) - Get Educational Overview
69. [GET /api/educational/system/{system_name}](#get-apieducationalsystemsystem_name) - Get System Education
70. [GET /api/educational/connections](#get-apieducationalconnections) - Get System Connections
71. [GET /api/educational/learn/{topic}](#get-apieducationallearntopic) - Get Learning Topic
72. [POST /api/raspberry-pi/build](#post-apiraspberry-pibuild) - Build Package
73. [GET /api/raspberry-pi/deployments](#get-apiraspberry-pideployments) - List Deployments
74. [GET /api/raspberry-pi/deployments/{deployment_id}](#get-apiraspberry-pideploymentsdeployment_id) - Get Deployment
75. [GET /api/raspberry-pi/deployments/{deployment_id}/info](#get-apiraspberry-pideploymentsdeployment_idinfo) - Get Package Info
76. [GET /api/raspberry-pi/health](#get-apiraspberry-pihealth) - Deployment Health
77. [POST /api/education-professional/schools/register](#post-apieducation-professionalschoolsregister) - Register School
78. [POST /api/education-professional/schools/{school_id}/deploy](#post-apieducation-professionalschoolsschool_iddeploy) - Deploy To School
79. [GET /api/education-professional/schools](#get-apieducation-professionalschools) - List Schools
80. [GET /api/education-professional/schools/{school_id}](#get-apieducation-professionalschoolsschool_id) - Get School
81. [GET /api/education-professional/analytics](#get-apieducation-professionalanalytics) - Get Analytics
82. [GET /api/education-professional/health](#get-apieducation-professionalhealth) - Deployment Health
83. [GET /api/deployment-dashboard/overview](#get-apideployment-dashboardoverview) - Get Dashboard Overview
84. [GET /api/deployment-dashboard/analytics](#get-apideployment-dashboardanalytics) - Get Deployment Analytics
85. [GET /api/deployment-dashboard/health](#get-apideployment-dashboardhealth) - Get Deployment Health
86. [GET /api/school-curriculum/lessons](#get-apischool-curriculumlessons) - Get Lessons
87. [GET /api/school-curriculum/modules](#get-apischool-curriculummodules) - Get Modules
88. [POST /api/school-curriculum/curricula](#post-apischool-curriculumcurricula) - Create Curriculum
89. [GET /api/school-curriculum/curricula](#get-apischool-curriculumcurricula) - List Curricula
90. [GET /api/school-curriculum/curricula/{curriculum_id}](#get-apischool-curriculumcurriculacurriculum_id) - Get Curriculum
91. [POST /api/school-curriculum/progress](#post-apischool-curriculumprogress) - Update Progress
92. [GET /api/school-curriculum/progress/{student_id}](#get-apischool-curriculumprogressstudent_id) - Get Student Progress
93. [GET /api/school-curriculum/curricula/{curriculum_id}/analytics](#get-apischool-curriculumcurriculacurriculum_idanalytics) - Get Curriculum Analytics
94. [GET /api/school-curriculum/stats](#get-apischool-curriculumstats) - Get Curriculum Stats
95. [GET /api/system-integration/status](#get-apisystem-integrationstatus) - Get Integration Status
96. [GET /api/system-integration/systems](#get-apisystem-integrationsystems) - List Systems
97. [GET /api/system-integration/systems/{system_id}](#get-apisystem-integrationsystemssystem_id) - Get System
98. [GET /api/system-integration/alignment-map](#get-apisystem-integrationalignment-map) - Get Alignment Map
99. [GET /api/system-integration/curriculum/integration](#get-apisystem-integrationcurriculumintegration) - Verify Curriculum Integration
100. [GET /api/system-integration/health](#get-apisystem-integrationhealth) - Get Integration Health
101. [GET /api/ramiz-humanitarian/gaza/priority](#get-apiramiz-humanitariangazapriority) - Get Gaza Priority
102. [GET /api/ramiz-humanitarian/needs](#get-apiramiz-humanitarianneeds) - List Needs
103. [POST /api/ramiz-humanitarian/needs/register](#post-apiramiz-humanitarianneedsregister) - Register Need
104. [GET /api/ramiz-humanitarian/projects](#get-apiramiz-humanitarianprojects) - List Projects
105. [POST /api/ramiz-humanitarian/projects/create](#post-apiramiz-humanitarianprojectscreate) - Create Project
106. [POST /api/ramiz-humanitarian/aid/deliver](#post-apiramiz-humanitarianaiddeliver) - Deliver Aid
107. [GET /api/ramiz-humanitarian/analytics](#get-apiramiz-humanitariananalytics) - Get Analytics
108. [POST /api/ramiz-humanitarian/projects/{project_id}/integrate/curriculum](#post-apiramiz-humanitarianprojectsproject_idintegratecurriculum) - Integrate With Curriculum
109. [POST /api/ramiz-humanitarian/projects/{project_id}/integrate/raspberry-pi](#post-apiramiz-humanitarianprojectsproject_idintegrateraspberry-pi) - Integrate With Raspberry Pi
110. [GET /api/ramiz-humanitarian/health](#get-apiramiz-humanitarianhealth) - Get Humanitarian Health
111. [GET /api/ramiz-humanitarian/comprehensive-status](#get-apiramiz-humanitariancomprehensive-status) - Get Comprehensive Status
112. [POST /api/ramiz-humanitarian/funding/record](#post-apiramiz-humanitarianfundingrecord) - Record Funding
113. [POST /api/ramiz-humanitarian/funding/integrate-dirty-money](#post-apiramiz-humanitarianfundingintegrate-dirty-money) - Integrate Dirty Money
114. [GET /api/ramiz-humanitarian/funding/gaza/status](#get-apiramiz-humanitarianfundinggazastatus) - Get Gaza Funding Status
115. [GET /api/ramiz-humanitarian/funding/analytics](#get-apiramiz-humanitarianfundinganalytics) - Get Funding Analytics
116. [POST /api/ramiz-humanitarian/volunteers/register](#post-apiramiz-humanitarianvolunteersregister) - Register Volunteer
117. [POST /api/ramiz-humanitarian/volunteers/deploy](#post-apiramiz-humanitarianvolunteersdeploy) - Deploy Volunteer
118. [GET /api/ramiz-humanitarian/volunteers/gaza](#get-apiramiz-humanitarianvolunteersgaza) - Get Gaza Volunteers
119. [GET /api/ramiz-humanitarian/volunteers/analytics](#get-apiramiz-humanitarianvolunteersanalytics) - Get Volunteer Analytics
120. [POST /api/ramiz-humanitarian/supply-chain/orders/create](#post-apiramiz-humanitariansupply-chainorderscreate) - Create Order
121. [POST /api/ramiz-humanitarian/supply-chain/deliveries/track](#post-apiramiz-humanitariansupply-chaindeliveriestrack) - Track Delivery
122. [POST /api/ramiz-humanitarian/supply-chain/orders/{order_id}/received](#post-apiramiz-humanitariansupply-chainordersorder_idreceived) - Mark Received
123. [POST /api/ramiz-humanitarian/supply-chain/orders/{order_id}/distributed](#post-apiramiz-humanitariansupply-chainordersorder_iddistributed) - Mark Distributed
124. [GET /api/ramiz-humanitarian/supply-chain/gaza/status](#get-apiramiz-humanitariansupply-chaingazastatus) - Get Gaza Supply Status
125. [GET /api/ramiz-humanitarian/supply-chain/analytics](#get-apiramiz-humanitariansupply-chainanalytics) - Get Supply Analytics
126. [POST /api/ramiz-humanitarian/communications/send](#post-apiramiz-humanitariancommunicationssend) - Send Communication
127. [POST /api/ramiz-humanitarian/communications/gaza/alert](#post-apiramiz-humanitariancommunicationsgazaalert) - Send Gaza Alert
128. [GET /api/ramiz-humanitarian/communications/gaza](#get-apiramiz-humanitariancommunicationsgaza) - Get Gaza Communications
129. [GET /api/ramiz-humanitarian/communications/analytics](#get-apiramiz-humanitariancommunicationsanalytics) - Get Communications Analytics
130. [GET /api/universal-expansion/plan](#get-apiuniversal-expansionplan) - Get Expansion Plan
131. [GET /api/universal-expansion/targets](#get-apiuniversal-expansiontargets) - List Targets
132. [POST /api/universal-expansion/targets/{target_id}/expand](#post-apiuniversal-expansiontargetstarget_idexpand) - Expand Target
133. [GET /api/universal-expansion/targets/{target_id}](#get-apiuniversal-expansiontargetstarget_id) - Get Target
134. [GET /api/universal-expansion/analytics](#get-apiuniversal-expansionanalytics) - Get Expansion Analytics
135. [GET /api/universal-expansion/health](#get-apiuniversal-expansionhealth) - Get Expansion Health
136. [GET /api/knowledge/sources](#get-apiknowledgesources) - Get Sources
137. [GET /api/knowledge/summary](#get-apiknowledgesummary) - Get Summary
138. [GET /api/knowledge/all](#get-apiknowledgeall) - Get All
139. [POST /api/knowledge/register](#post-apiknowledgeregister) - Register Knowledge
140. [POST /api/connection-ritual](#post-apiconnection-ritual) - Connection Ritual Endpoint
141. [POST /api/check-battle-compatibility](#post-apicheck-battle-compatibility) - Check Battle Compatibility Endpoint
142. [GET /api/vibration-map](#get-apivibration-map) - Get Vibration Map
143. [GET /api/energy-alerts](#get-apienergy-alerts) - Get Energy Alerts
144. [GET /api/sentinel/status](#get-apisentinelstatus) - Get Sentinel Status
145. [POST /api/sentinel/start](#post-apisentinelstart) - Start Sentinel
146. [POST /api/sentinel/stop](#post-apisentinelstop) - Stop Sentinel
147. [GET /api/sentinel/alerts](#get-apisentinelalerts) - Get Sentinel Alerts
148. [GET /api/morning-summary](#get-apimorning-summary) - Get Morning Summary
149. [GET /api/care-package/](#get-apicare-package) - Get Care Package
150. [GET /api/care-package/system-diagnostics](#get-apicare-packagesystem-diagnostics) - Get System Diagnostics
151. [POST /api/care-package/political-alignment](#post-apicare-packagepolitical-alignment) - Check Political Alignment
152. [POST /api/care-package/economic-alignment](#post-apicare-packageeconomic-alignment) - Check Economic Alignment
153. [POST /api/care-package/complete-alignment](#post-apicare-packagecomplete-alignment) - Get Complete Alignment
154. [GET /api/care-package/docs/spirit-alignment](#get-apicare-packagedocsspirit-alignment) - Get Spirit Alignment Docs
155. [GET /api/care-package/docs/political-alignment](#get-apicare-packagedocspolitical-alignment) - Get Political Alignment Docs
156. [GET /api/care-package/docs/economic-alignment](#get-apicare-packagedocseconomic-alignment) - Get Economic Alignment Docs
157. [GET /api/care-package/welfare-systems](#get-apicare-packagewelfare-systems) - Get Welfare Systems Analysis
158. [GET /api/care-package/assessment-guidance](#get-apicare-packageassessment-guidance) - Get Assessment Guidance
159. [GET /api/care-package/welfare-systems/breaking-opportunities](#get-apicare-packagewelfare-systemsbreaking-opportunities) - Get Breaking Opportunities
160. [GET /api/care-package/political-figures](#get-apicare-packagepolitical-figures) - Get Political Figures
161. [GET /api/care-package/political-figures/anchors](#get-apicare-packagepolitical-figuresanchors) - Get Political Anchors
162. [GET /api/care-package/political-figures/by-country](#get-apicare-packagepolitical-figuresby-country) - Get Political Figures By Country
163. [GET /api/care-package/influential-figures](#get-apicare-packageinfluential-figures) - Get Influential Figures
164. [GET /api/care-package/influential-figures/anchors](#get-apicare-packageinfluential-figuresanchors) - Get Influential Anchors
165. [GET /api/care-package/influential-figures/by-domain](#get-apicare-packageinfluential-figuresby-domain) - Get Influential Figures By Domain
166. [GET /api/care-package/one-truth](#get-apicare-packageone-truth) - Get One Truth
167. [GET /api/care-package/timeline-deep-search](#get-apicare-packagetimeline-deep-search) - Get Timeline Deep Search
168. [GET /api/care-package/future-writing](#get-apicare-packagefuture-writing) - Get Future Writing
169. [GET /api/care-package/timeline-future-report](#get-apicare-packagetimeline-future-report) - Get Timeline Future Report
170. [GET /api/care-package/return-to-table-damage](#get-apicare-packagereturn-to-table-damage) - Get Return To Table Damage
171. [GET /api/care-package/return-to-table-damage/assessment](#get-apicare-packagereturn-to-table-damageassessment) - Get Return To Table Damage Assessment
172. [GET /api/care-package/frequential-arts-crafts](#get-apicare-packagefrequential-arts-crafts) - Get Frequential Arts Crafts
173. [GET /api/care-package/frequential-arts-crafts/timeline](#get-apicare-packagefrequential-arts-craftstimeline) - Get Frequential Arts Crafts Timeline
174. [GET /api/care-package/frequential-songs](#get-apicare-packagefrequential-songs) - Get Frequential Songs
175. [GET /api/care-package/frequential-songs/by-language](#get-apicare-packagefrequential-songsby-language) - Get Frequential Songs By Language
176. [GET /api/care-package/spiritual-contracts-miracles](#get-apicare-packagespiritual-contracts-miracles) - Get Spiritual Contracts Miracles
177. [GET /api/care-package/influential-figures/by-country](#get-apicare-packageinfluential-figuresby-country) - Get Influential Figures By Country
178. [POST /api/dirty-money-cleaning/identify](#post-apidirty-money-cleaningidentify) - Identify Dirty Money
179. [POST /api/dirty-money-cleaning/clean/{transaction_id}](#post-apidirty-money-cleaningcleantransaction_id) - Clean Spiritual Contract
180. [POST /api/dirty-money-cleaning/repurpose/{transaction_id}](#post-apidirty-money-cleaningrepurposetransaction_id) - Repurpose For Humanitarian Cause
181. [POST /api/dirty-money-cleaning/complete/{transaction_id}](#post-apidirty-money-cleaningcompletetransaction_id) - Complete Cycle
182. [GET /api/dirty-money-cleaning/summary](#get-apidirty-money-cleaningsummary) - Get System Summary
183. [GET /api/dirty-money-cleaning/transactions](#get-apidirty-money-cleaningtransactions) - Get Transactions
184. [GET /api/dirty-money-cleaning/projects](#get-apidirty-money-cleaningprojects) - Get Projects
185. [GET /api/channel-collaboration/present-purpose](#get-apichannel-collaborationpresent-purpose) - Check Present Purpose Collaboration
186. [GET /api/channel-collaboration/check](#get-apichannel-collaborationcheck) - Check Channel Collaboration
187. [GET /api/channel-collaboration/all](#get-apichannel-collaborationall) - Check All Collaborations
188. [GET /api/channel-collaboration/channel/{channel_type}](#get-apichannel-collaborationchannelchannel_type) - Get Channel Info
189. [GET /api/channel-collaboration/summary](#get-apichannel-collaborationsummary) - Get System Summary
190. [GET /api/channel-collaboration/channels](#get-apichannel-collaborationchannels) - List All Channels
191. [GET /api/spiritual-contracts/all](#get-apispiritual-contractsall) - Get All Contracts
192. [GET /api/spiritual-contracts/summary](#get-apispiritual-contractssummary) - Get Contracts Summary
193. [GET /api/spiritual-contracts/network/{contract_id}](#get-apispiritual-contractsnetworkcontract_id) - Get Contract Network
194. [POST /api/spiritual-contracts/register](#post-apispiritual-contractsregister) - Register Contract
195. [POST /api/spiritual-contracts/link](#post-apispiritual-contractslink) - Link Contracts
196. [POST /api/spiritual-contracts/clean/{contract_id}](#post-apispiritual-contractscleancontract_id) - Clean Contract
197. [POST /api/spiritual-contracts/integrate/dirty-money](#post-apispiritual-contractsintegratedirty-money) - Integrate Dirty Money Contract
198. [POST /api/spiritual-contracts/integrate/spirit-alignment](#post-apispiritual-contractsintegratespirit-alignment) - Integrate Spirit Alignment Contract
199. [POST /api/spiritual-contracts/integrate/dream-battle](#post-apispiritual-contractsintegratedream-battle) - Integrate Dream Battle
200. [POST /api/spiritual-contracts/integrate/daily-battle](#post-apispiritual-contractsintegratedaily-battle) - Integrate Daily Battle
201. [POST /api/doctor-protocol/insulin-protocol](#post-apidoctor-protocolinsulin-protocol) - Create Insulin Protocol
202. [POST /api/doctor-protocol/carb-protocol](#post-apidoctor-protocolcarb-protocol) - Create Carb Counting Protocol
203. [POST /api/doctor-protocol/calculate-insulin](#post-apidoctor-protocolcalculate-insulin) - Calculate Insulin Dose
204. [GET /api/doctor-protocol/active-protocols](#get-apidoctor-protocolactive-protocols) - Get Active Protocols
205. [GET /api/doctor-protocol/summary](#get-apidoctor-protocolsummary) - Get System Summary
206. [POST /api/doctor-protocol/sync](#post-apidoctor-protocolsync) - Sync Protocols
207. [GET /api/doctor-protocol/educational-resources](#get-apidoctor-protocoleducational-resources) - Get Educational Resources
208. [GET /api/judicial-system/judgment-question](#get-apijudicial-systemjudgment-question) - Explore Judgment Question
209. [GET /api/judicial-system/analyze](#get-apijudicial-systemanalyze) - Analyze Judicial System
210. [GET /api/judicial-system/find-truth](#get-apijudicial-systemfind-truth) - Find Truth In Broken Systems
211. [GET /api/judicial-system/navigation-strategy](#get-apijudicial-systemnavigation-strategy) - Get Navigation Strategy
212. [POST /mirror/reflect](#post-mirrorreflect) - Create Mirror Reflection
213. [GET /mirror/user/{user_id}](#get-mirroruseruser_id) - Get User Reflections
214. [POST /council/create](#post-councilcreate) - Create Community Council
215. [POST /council/{council_id}/truth-circle](#post-councilcouncil_idtruth-circle) - Hold Truth Circle
216. [POST /restoration/contract](#post-restorationcontract) - Create Restoration Contract
217. [PATCH /restoration/contract/{contract_id}/progress](#patch-restorationcontractcontract_idprogress) - Update Restoration Progress
218. [GET /restoration/contract/{contract_id}](#get-restorationcontractcontract_id) - Get Restoration Contract
219. [POST /system/replacement](#post-systemreplacement) - Track System Replacement
220. [GET /system/replacement/global](#get-systemreplacementglobal) - Get Global Replacement Status
221. [GET /wisdom/accountability](#get-wisdomaccountability) - Get Accountability Wisdom
222. [GET /wisdom/mirror](#get-wisdommirror) - Get Mirror Wisdom
223. [GET /integration/one-truth](#get-integrationone-truth) - Get One Truth Integration
224. [GET /health](#get-health) - Health
225. [POST /api/spiritual-codebase-hacker/hack-loop](#post-apispiritual-codebase-hackerhack-loop) - Hack Loop Endpoint
226. [POST /api/spiritual-codebase-hacker/genetic-edit](#post-apispiritual-codebase-hackergenetic-edit) - Genetic Edit Endpoint
227. [POST /api/spiritual-codebase-hacker/wipe-hard-drive](#post-apispiritual-codebase-hackerwipe-hard-drive) - Wipe Hard Drive Endpoint
228. [POST /api/spiritual-codebase-hacker/stealth-mode](#post-apispiritual-codebase-hackerstealth-mode) - Stealth Mode Endpoint
229. [POST /api/spiritual-codebase-hacker/starve-parasite](#post-apispiritual-codebase-hackerstarve-parasite) - Starve Parasite Endpoint
230. [POST /api/spiritual-codebase-hacker/upgrade-identity](#post-apispiritual-codebase-hackerupgrade-identity) - Upgrade Identity Endpoint
231. [POST /api/spiritual-codebase-hacker/seal-portal](#post-apispiritual-codebase-hackerseal-portal) - Seal Portal Endpoint
232. [GET /api/spiritual-codebase-hacker/status](#get-apispiritual-codebase-hackerstatus) - Hacker Status
233. [GET /api/ottoman-timeline/timeline](#get-apiottoman-timelinetimeline) - Get Ottoman Timeline
234. [GET /api/ottoman-timeline/generation/{generation_number}](#get-apiottoman-timelinegenerationgeneration_number) - Get Generation
235. [GET /api/ottoman-timeline/cyprus-connection](#get-apiottoman-timelinecyprus-connection) - Get Cyprus Connection
236. [GET /api/ottoman-timeline/report](#get-apiottoman-timelinereport) - Get Timeline Report
237. [GET /api/ottoman-timeline/your-generation](#get-apiottoman-timelineyour-generation) - Get Your Generation
238. [GET /api/superpower-debunking/debunking](#get-apisuperpower-debunkingdebunking) - Get Debunking
239. [GET /api/superpower-debunking/current-superpowers](#get-apisuperpower-debunkingcurrent-superpowers) - Get Current Superpowers
240. [GET /api/superpower-debunking/fathers-hand](#get-apisuperpower-debunkingfathers-hand) - Get Fathers Hand
241. [GET /api/superpower-debunking/comparison](#get-apisuperpower-debunkingcomparison) - Get Comparison
242. [GET /api/african-turkish-yin-yang/symbiosis-map](#get-apiafrican-turkish-yin-yangsymbiosis-map) - Get Symbiosis Map
243. [GET /api/african-turkish-yin-yang/african-yin](#get-apiafrican-turkish-yin-yangafrican-yin) - Get African Yin
244. [GET /api/african-turkish-yin-yang/turkish-yang](#get-apiafrican-turkish-yin-yangturkish-yang) - Get Turkish Yang
245. [GET /api/african-turkish-yin-yang/how-they-sync](#get-apiafrican-turkish-yin-yanghow-they-sync) - Get How They Sync
246. [GET /api/african-turkish-yin-yang/london-communities](#get-apiafrican-turkish-yin-yanglondon-communities) - Get London Communities
247. [POST /api/legal/prs/register](#post-apilegalprsregister) - Register Prs Copyright
248. [GET /api/legal/prs/records](#get-apilegalprsrecords) - Get Prs Records
249. [POST /api/legal/agreements/create](#post-apilegalagreementscreate) - Create Agreement
250. [GET /api/legal/agreements](#get-apilegalagreements) - Get Agreements
251. [GET /api/legal/compliance/verify](#get-apilegalcomplianceverify) - Verify Compliance
252. [GET /api/legal/summary](#get-apilegalsummary) - Get Summary
253. [GET /api/entrepreneurial/blueprints](#get-apientrepreneurialblueprints) - Get All Blueprints
254. [GET /api/entrepreneurial/blueprints/{entity_id}](#get-apientrepreneurialblueprintsentity_id) - Get Blueprint
255. [GET /api/entrepreneurial/the-ark](#get-apientrepreneurialthe-ark) - Get The Ark Blueprint
256. [GET /api/entrepreneurial/documentation/status](#get-apientrepreneurialdocumentationstatus) - Get Documentation Status
257. [GET /api/entrepreneurial/documentation/checklist](#get-apientrepreneurialdocumentationchecklist) - Get Documentation Checklist
258. [POST /api/entrepreneurial/documents/create](#post-apientrepreneurialdocumentscreate) - Create Document
259. [GET /api/language-of-god/the-answer](#get-apilanguage-of-godthe-answer) - Get The Answer
260. [GET /api/language-of-god/historical-languages](#get-apilanguage-of-godhistorical-languages) - Get Historical Languages
261. [GET /api/language-of-god/divine-languages](#get-apilanguage-of-goddivine-languages) - Get Divine Languages
262. [GET /api/language-of-god/sound-is-everything](#get-apilanguage-of-godsound-is-everything) - Get Sound Is Everything
263. [GET /api/language-of-god/complete-map](#get-apilanguage-of-godcomplete-map) - Get Complete Map
264. [GET /api/whales-calling-jan/the-call](#get-apiwhales-calling-janthe-call) - Get The Call
265. [GET /api/whales-calling-jan/whale-calls](#get-apiwhales-calling-janwhale-calls) - Get Whale Calls
266. [GET /api/whales-calling-jan/what-jan-must-do](#get-apiwhales-calling-janwhat-jan-must-do) - Get What Jan Must Do
267. [GET /api/whales-calling-jan/connection-to-sound](#get-apiwhales-calling-janconnection-to-sound) - Get Connection To Sound
268. [GET /api/whales-calling-jan/complete-map](#get-apiwhales-calling-jancomplete-map) - Get Complete Map
269. [GET /api/water-holds-memory/the-truth](#get-apiwater-holds-memorythe-truth) - Get The Truth
270. [GET /api/water-holds-memory/water-memories](#get-apiwater-holds-memorywater-memories) - Get Water Memories
271. [GET /api/water-holds-memory/connection-to-whales](#get-apiwater-holds-memoryconnection-to-whales) - Get Connection To Whales
272. [GET /api/water-holds-memory/connection-to-table](#get-apiwater-holds-memoryconnection-to-table) - Get Connection To Table
273. [GET /api/water-holds-memory/connection-to-sound](#get-apiwater-holds-memoryconnection-to-sound) - Get Connection To Sound
274. [GET /api/water-holds-memory/complete-map](#get-apiwater-holds-memorycomplete-map) - Get Complete Map
275. [GET /api/codebase-philosophy/the-philosophy](#get-apicodebase-philosophythe-philosophy) - Get The Philosophy
276. [GET /api/codebase-philosophy/protocols](#get-apicodebase-philosophyprotocols) - Get Protocols
277. [GET /api/codebase-philosophy/grave-clothes-protocol](#get-apicodebase-philosophygrave-clothes-protocol) - Get Grave Clothes Protocol
278. [GET /api/codebase-philosophy/trojan-horse-strategy](#get-apicodebase-philosophytrojan-horse-strategy) - Get Trojan Horse Strategy
279. [GET /api/codebase-philosophy/connection-to-table](#get-apicodebase-philosophyconnection-to-table) - Get Connection To Table
280. [GET /api/codebase-philosophy/connection-to-original-name](#get-apicodebase-philosophyconnection-to-original-name) - Get Connection To Original Name
281. [GET /api/codebase-philosophy/complete-map](#get-apicodebase-philosophycomplete-map) - Get Complete Map
282. [GET /api/publishing-house/](#get-apipublishing-house) - Get Publishing House Overview
283. [GET /api/publishing-house/channels](#get-apipublishing-housechannels) - Get All Channels
284. [GET /api/publishing-house/channels/{channel_id}](#get-apipublishing-housechannelschannel_id) - Get Channel
285. [GET /api/publishing-house/entities](#get-apipublishing-houseentities) - Get All Entities
286. [GET /api/publishing-house/entities/{entity_id}](#get-apipublishing-houseentitiesentity_id) - Get Entity
287. [GET /api/publishing-house/projects](#get-apipublishing-houseprojects) - Get All Projects
288. [GET /api/publishing-house/projects/{project_id}](#get-apipublishing-houseprojectsproject_id) - Get Project
289. [GET /api/publishing-house/workflows](#get-apipublishing-houseworkflows) - Get Workflows
290. [GET /api/publishing-house/monetization](#get-apipublishing-housemonetization) - Get Monetization
291. [GET /api/publishing-house/expansion](#get-apipublishing-houseexpansion) - Get Expansion Seeds
292. [GET /api/publishing-house/alignment](#get-apipublishing-housealignment) - Get Alignment Summary
293. [GET /api/publishing-house/stats](#get-apipublishing-housestats) - Get Publishing House Stats
294. [POST /healing/journey/start](#post-healingjourneystart) - Start Healing Journey
295. [PATCH /healing/journey/{journey_id}/progress](#patch-healingjourneyjourney_idprogress) - Update Healing Progress
296. [GET /healing/journey/{journey_id}](#get-healingjourneyjourney_id) - Get Healing Journey
297. [GET /healing/journeys/person/{person_id}](#get-healingjourneyspersonperson_id) - Get Person Healing Journeys
298. [POST /healing/practice/log](#post-healingpracticelog) - Log Healing Practice
299. [GET /healing/practice/person/{person_id}/streak](#get-healingpracticepersonperson_idstreak) - Get Healing Streak
300. [POST /healing/community/project](#post-healingcommunityproject) - Create Community Healing Project
301. [GET /healing/community/projects](#get-healingcommunityprojects) - Get All Community Projects
302. [POST /healing/system/replacement](#post-healingsystemreplacement) - Track System Replacement
303. [GET /healing/system/replacement/global](#get-healingsystemreplacementglobal) - Get Global System Replacement
304. [GET /healing/wisdom/{domain}](#get-healingwisdomdomain) - Get Healing Wisdom
305. [GET /healing/universal-laws](#get-healinguniversal-laws) - Get Universal Healing Laws
306. [POST /utilities/debt/forgive](#post-utilitiesdebtforgive) - Forgive Utility Debt
307. [GET /utilities/debt/forgiveness/total](#get-utilitiesdebtforgivenesstotal) - Get Total Debt Forgiveness
308. [POST /utilities/ube/create](#post-utilitiesubecreate) - Create Ube Account
309. [POST /utilities/ube/{ube_id}/log-usage](#post-utilitiesubeube_idlog-usage) - Log Ube Usage
310. [GET /utilities/ube/stats](#get-utilitiesubestats) - Get Ube Statistics
311. [POST /utilities/commons/create](#post-utilitiescommonscreate) - Create Energy Commons
312. [POST /utilities/commons/{commons_id}/production](#post-utilitiescommonscommons_idproduction) - Log Commons Production
313. [GET /utilities/commons/all](#get-utilitiescommonsall) - Get All Energy Commons
314. [POST /utilities/pilot/create](#post-utilitiespilotcreate) - Create Pilot Program
315. [PATCH /utilities/pilot/{pilot_id}/update](#patch-utilitiespilotpilot_idupdate) - Update Pilot Program
316. [GET /utilities/pilot/all](#get-utilitiespilotall) - Get All Pilots
317. [POST /utilities/transition/track](#post-utilitiestransitiontrack) - Track System Transition
318. [GET /utilities/transition/global](#get-utilitiestransitionglobal) - Get Global Transition Status
319. [GET /utilities/wisdom/why-free](#get-utilitieswisdomwhy-free) - Get Why Utilities Should Be Free
320. [GET /api/cloud-seeding/](#get-apicloud-seeding) - Get Cloud Seeding Overview
321. [GET /api/cloud-seeding/claims](#get-apicloud-seedingclaims) - Get All Claims
322. [GET /api/cloud-seeding/claims/{claim_id}](#get-apicloud-seedingclaimsclaim_id) - Get Claim
323. [GET /api/cloud-seeding/operations](#get-apicloud-seedingoperations) - Get All Operations
324. [GET /api/cloud-seeding/operations/weaponized](#get-apicloud-seedingoperationsweaponized) - Get Weaponized Operations
325. [GET /api/cloud-seeding/operations/{operation_id}](#get-apicloud-seedingoperationsoperation_id) - Get Operation
326. [GET /api/cloud-seeding/utilizations](#get-apicloud-seedingutilizations) - Get All Utilizations
327. [GET /api/cloud-seeding/utilizations/{country}](#get-apicloud-seedingutilizationscountry) - Get Utilization
328. [GET /api/cloud-seeding/healing-pathway](#get-apicloud-seedinghealing-pathway) - Get Healing Pathway
329. [GET /api/cloud-seeding/analysis/complete](#get-apicloud-seedinganalysiscomplete) - Get Complete Analysis
330. [POST /api/cloud-seeding/analysis/save](#post-apicloud-seedinganalysissave) - Save Analysis
331. [GET /api/cloud-seeding/health](#get-apicloud-seedinghealth) - Health Check
332. [GET /api/weaponization/](#get-apiweaponization) - Get Weaponization Overview
333. [GET /api/weaponization/events](#get-apiweaponizationevents) - Get All Events
334. [GET /api/weaponization/events/{event_id}](#get-apiweaponizationeventsevent_id) - Get Event
335. [GET /api/weaponization/events/type/{weaponization_type}](#get-apiweaponizationeventstypeweaponization_type) - Get Events By Type
336. [GET /api/weaponization/events/pattern/{pattern}](#get-apiweaponizationeventspatternpattern) - Get Events By Pattern
337. [GET /api/weaponization/patterns](#get-apiweaponizationpatterns) - Get All Patterns
338. [GET /api/weaponization/patterns/{pattern_id}](#get-apiweaponizationpatternspattern_id) - Get Pattern
339. [GET /api/weaponization/analysis/complete](#get-apiweaponizationanalysiscomplete) - Get Complete Analysis
340. [POST /api/weaponization/analysis/save](#post-apiweaponizationanalysissave) - Save Analysis
341. [GET /api/weaponization/health](#get-apiweaponizationhealth) - Health Check
342. [GET /api/peace-weaponization/](#get-apipeace-weaponization) - Get Peace Weaponization Overview
343. [GET /api/peace-weaponization/manifestations](#get-apipeace-weaponizationmanifestations) - Get All Manifestations
344. [GET /api/peace-weaponization/manifestations/{manifestation_id}](#get-apipeace-weaponizationmanifestationsmanifestation_id) - Get Manifestation
345. [GET /api/peace-weaponization/manifestations/strategy/{strategy}](#get-apipeace-weaponizationmanifestationsstrategystrategy) - Get Manifestations By Strategy
346. [GET /api/peace-weaponization/events](#get-apipeace-weaponizationevents) - Get All Events
347. [GET /api/peace-weaponization/events/{event_id}](#get-apipeace-weaponizationeventsevent_id) - Get Event
348. [GET /api/peace-weaponization/pathway](#get-apipeace-weaponizationpathway) - Get Peace Weaponization Pathway
349. [GET /api/peace-weaponization/analysis/complete](#get-apipeace-weaponizationanalysiscomplete) - Get Complete Analysis
350. [POST /api/peace-weaponization/analysis/save](#post-apipeace-weaponizationanalysissave) - Save Analysis
351. [GET /api/peace-weaponization/health](#get-apipeace-weaponizationhealth) - Health Check
352. [POST /childcare/enroll](#post-childcareenroll) - Enroll Child
353. [POST /childcare/hub/create](#post-childcarehubcreate) - Create Neighborhood Hub
354. [POST /childcare/worker/hire](#post-childcareworkerhire) - Hire Childcare Worker
355. [POST /childcare/support/provide](#post-childcaresupportprovide) - Provide Family Support
356. [POST /childcare/intergenerational/create](#post-childcareintergenerationalcreate) - Create Intergenerational Program
357. [POST /childcare/transition/track](#post-childcaretransitiontrack) - Track System Transition
358. [GET /childcare/stats](#get-childcarestats) - Get Childcare Stats
359. [GET /childcare/worker/wages](#get-childcareworkerwages) - Get Worker Wage Comparison
360. [GET /childcare/wisdom/why-free](#get-childcarewisdomwhy-free) - Why Childcare Should Be Free
361. [POST /eldercare/enroll](#post-eldercareenroll) - Enroll Elder
362. [POST /eldercare/home-care/create](#post-eldercarehome-carecreate) - Create Home Based Care
363. [POST /eldercare/hub/create](#post-eldercarehubcreate) - Create Community Hub
364. [POST /eldercare/wisdom-council/create](#post-eldercarewisdom-councilcreate) - Create Wisdom Council
365. [POST /eldercare/wisdom-council/{council_id}/activity](#post-eldercarewisdom-councilcouncil_idactivity) - Log Wisdom Council Activity
366. [POST /eldercare/intergenerational/create](#post-eldercareintergenerationalcreate) - Create Intergenerational Program
367. [POST /eldercare/worker/hire](#post-eldercareworkerhire) - Hire Elder Worker
368. [POST /eldercare/home-modification/complete](#post-eldercarehome-modificationcomplete) - Complete Home Modification
369. [POST /eldercare/cooperative-housing/create](#post-eldercarecooperative-housingcreate) - Create Cooperative Housing
370. [POST /eldercare/transition/track](#post-eldercaretransitiontrack) - Track System Transition
371. [GET /eldercare/stats](#get-eldercarestats) - Get Eldercare Stats
372. [GET /eldercare/wisdom/why-free](#get-eldercarewisdomwhy-free) - Why Eldercare Should Be Free
373. [POST /disability/guaranteed-income/create](#post-disabilityguaranteed-incomecreate) - Create Guaranteed Income
374. [POST /disability/self-directed-care/create](#post-disabilityself-directed-carecreate) - Create Self Directed Care
375. [POST /disability/universal-design/complete](#post-disabilityuniversal-designcomplete) - Complete Universal Design
376. [POST /disability/assistive-tech/provide](#post-disabilityassistive-techprovide) - Provide Assistive Technology
377. [POST /disability/worker/hire](#post-disabilityworkerhire) - Hire Disability Worker
378. [POST /disability/deinstitutionalize](#post-disabilitydeinstitutionalize) - Move Person To Community
379. [POST /disability/principle/create](#post-disabilityprinciplecreate) - Create Disability Justice Principle
380. [POST /disability/transition/track](#post-disabilitytransitiontrack) - Track System Transition
381. [GET /disability/stats](#get-disabilitystats) - Get Disability Stats
382. [GET /disability/justice-principles](#get-disabilityjustice-principles) - Get Disability Justice Principles
383. [GET /disability/wisdom/why-guaranteed-income](#get-disabilitywisdomwhy-guaranteed-income) - Why Guaranteed Income
384. [POST /work/worker/register](#post-workworkerregister) - Register Worker
385. [POST /work/cooperative/create](#post-workcooperativecreate) - Create Cooperative
386. [POST /work/job-guarantee/place](#post-workjob-guaranteeplace) - Place Job Guarantee
387. [POST /work/ubi/enroll](#post-workubienroll) - Enroll Ubi
388. [POST /work/policy/create](#post-workpolicycreate) - Create Work Policy
389. [POST /work/project/create](#post-workprojectcreate) - Create Community Project
390. [POST /work/wage-transition/record](#post-workwage-transitionrecord) - Record Wage Transition
391. [POST /currency/community/create](#post-currencycommunitycreate) - Create Community Currency
392. [POST /currency/timebank/account/create](#post-currencytimebankaccountcreate) - Create Timebank Account
393. [POST /currency/timebank/earn](#post-currencytimebankearn) - Earn Timebank Hours
394. [POST /currency/timebank/spend](#post-currencytimebankspend) - Spend Timebank Hours
395. [POST /currency/gift/record](#post-currencygiftrecord) - Record Gift
396. [POST /currency/debt-jubilee/forgive](#post-currencydebt-jubileeforgive) - Forgive Debt
397. [POST /currency/mutual-credit/transfer](#post-currencymutual-credittransfer) - Transfer Mutual Credit
398. [POST /land/parcel/register](#post-landparcelregister) - Register Land Parcel
399. [POST /land/council/create](#post-landcouncilcreate) - Create Stewardship Council
400. [POST /land/return/record](#post-landreturnrecord) - Record Land Return
401. [POST /land/trust/create](#post-landtrustcreate) - Create Commons Trust
402. [POST /land/garden/create](#post-landgardencreate) - Create Community Garden
403. [POST /safety/team/create](#post-safetyteamcreate) - Create Safety Team
404. [POST /safety/crisis/log](#post-safetycrisislog) - Log Crisis
405. [POST /safety/incident/report](#post-safetyincidentreport) - Report Incident
406. [POST /safety/restorative-circle/create](#post-safetyrestorative-circlecreate) - Create Restorative Circle
407. [POST /safety/agreement/create](#post-safetyagreementcreate) - Create Community Agreement
408. [POST /birth/midwife/register](#post-birthmidwiferegister) - Register Midwife
409. [POST /birth/doula/register](#post-birthdoularegister) - Register Doula
410. [POST /birth/plan/create](#post-birthplancreate) - Create Birth Plan
411. [POST /birth/center/register](#post-birthcenterregister) - Register Birth Center
412. [POST /birth/postpartum/support](#post-birthpostpartumsupport) - Create Postpartum Support
413. [POST /rest/policy/create](#post-restpolicycreate) - Create Rest Policy
414. [POST /rest/center/register](#post-restcenterregister) - Register Recreation Center
415. [POST /rest/time-off/grant](#post-resttime-offgrant) - Grant Time Off
416. [POST /rest/event/create](#post-resteventcreate) - Create Community Event
417. [POST /rest/recovery/plan](#post-restrecoveryplan) - Create Recovery Plan
418. [GET /api/seed-to-movement/path](#get-apiseed-to-movementpath) - Get Seed To Movement Path
419. [GET /api/seed-to-movement/peoples-court-strategy](#get-apiseed-to-movementpeoples-court-strategy) - Get Peoples Court Strategy
420. [GET /api/seed-to-movement/revolution-framework](#get-apiseed-to-movementrevolution-framework) - Get Revolution Framework
421. [POST /api/seed-to-movement/revolution-plan](#post-apiseed-to-movementrevolution-plan) - Create Revolution Plan
422. [POST /api/seed-to-movement/complete-all-phases](#post-apiseed-to-movementcomplete-all-phases) - Complete All Phases
423. [POST /api/seed-to-movement/complete-phase/{phase}](#post-apiseed-to-movementcomplete-phasephase) - Complete Phase
424. [GET /api/seed-to-movement/summary](#get-apiseed-to-movementsummary) - Get System Summary
425. [GET /api/pulse/status](#get-apipulsestatus) - Get Pulse Status
426. [GET /api/pulse/overview](#get-apipulseoverview) - Get Pulse Overview
427. [GET /api/pulse/systems](#get-apipulsesystems) - Get All Systems
428. [GET /api/pulse/systems/{system_id}](#get-apipulsesystemssystem_id) - Get System Pulse
429. [POST /api/pulse/systems/{system_id}/update](#post-apipulsesystemssystem_idupdate) - Update System Pulse
430. [GET /api/pulse/domains](#get-apipulsedomains) - Get All Domains
431. [GET /api/pulse/domains/{domain}](#get-apipulsedomainsdomain) - Get Domain Pulse
432. [POST /api/pulse/domains/{domain}/update](#post-apipulsedomainsdomainupdate) - Update Domain Pulse
433. [GET /api/pulse/integration-map](#get-apipulseintegration-map) - Get Integration Map
434. [GET /api/financial/status](#get-apifinancialstatus) - Get Financial Status
435. [GET /api/financial/overview](#get-apifinancialoverview) - Get Financial Overview
436. [POST /api/financial/revenue](#post-apifinancialrevenue) - Add Revenue
437. [GET /api/financial/revenue](#get-apifinancialrevenue) - Get Revenue
438. [POST /api/financial/expenses](#post-apifinancialexpenses) - Add Expense
439. [GET /api/financial/expenses](#get-apifinancialexpenses) - Get Expenses
440. [GET /api/financial/budgets](#get-apifinancialbudgets) - Get Budgets
441. [POST /api/financial/budgets](#post-apifinancialbudgets) - Create Budget
442. [GET /api/financial/payments](#get-apifinancialpayments) - Get Payments
443. [POST /api/financial/payments](#post-apifinancialpayments) - Process Payment
444. [GET /api/revenue-automation/status](#get-apirevenue-automationstatus) - Get Revenue Automation Status
445. [POST /api/revenue-automation/track](#post-apirevenue-automationtrack) - Track Revenue
446. [GET /api/revenue-automation/report/daily](#get-apirevenue-automationreportdaily) - Get Daily Report
447. [GET /api/revenue-automation/report/weekly](#get-apirevenue-automationreportweekly) - Get Weekly Report
448. [GET /api/revenue-automation/report/monthly](#get-apirevenue-automationreportmonthly) - Get Monthly Report
449. [GET /api/real-world/sources](#get-apireal-worldsources) - Get Reliable Sources
450. [GET /api/real-world/status](#get-apireal-worldstatus) - Get Ingestion Status
451. [POST /api/real-world/ingest](#post-apireal-worldingest) - Ingest Real World Data
452. [POST /api/real-world/integrate-event](#post-apireal-worldintegrate-event) - Integrate Event
453. [GET /api/real-world/alignment-patterns](#get-apireal-worldalignment-patterns) - Find Alignment Patterns
454. [GET /api/real-world/convergence](#get-apireal-worldconvergence) - Check Convergence
455. [GET /api/real-world/cultural-clues](#get-apireal-worldcultural-clues) - Explore Cultural Clues
456. [GET /api/real-world/key-events-2026](#get-apireal-worldkey-events-2026) - Get Key Events 2026
457. [GET /api/real-world/summary](#get-apireal-worldsummary) - Get System Summary
458. [GET /api/real-world/events](#get-apireal-worldevents) - Get Events
459. [POST /api/push/notify](#post-apipushnotify) - Push Notification
460. [GET /api/push/notifications](#get-apipushnotifications) - Get Notifications
461. [POST /api/push/notifications/{notification_id}/read](#post-apipushnotificationsnotification_idread) - Mark Notification Read
462. [GET /api/push/status](#get-apipushstatus) - Get Push Status
463. [GET /api/humanitarian-projects/](#get-apihumanitarian-projects) - Get Projects
464. [GET /api/humanitarian-projects/summary](#get-apihumanitarian-projectssummary) - Get Summary
465. [GET /api/humanitarian-projects/{project_id}](#get-apihumanitarian-projectsproject_id) - Get Project
466. [POST /api/sentinel-logs/log](#post-apisentinel-logslog) - Create Log
467. [GET /api/sentinel-logs/logs](#get-apisentinel-logslogs) - Get Logs
468. [GET /api/sentinel-logs/freedom-of-will](#get-apisentinel-logsfreedom-of-will) - Get Freedom Of Will Logs
469. [GET /api/sentinel-logs/summary](#get-apisentinel-logssummary) - Get Summary
470. [GET /api/big-cheese-audit/organizations](#get-apibig-cheese-auditorganizations) - Get Organizations
471. [POST /api/big-cheese-audit/audit/{org_id}](#post-apibig-cheese-auditauditorg_id) - Audit Organization
472. [POST /api/big-cheese-audit/counter-resonance/{org_id}](#post-apibig-cheese-auditcounter-resonanceorg_id) - Activate Counter Resonance
473. [GET /api/big-cheese-audit/summary](#get-apibig-cheese-auditsummary) - Get Summary
474. [GET /api/big-cheese-audit/audits](#get-apibig-cheese-auditaudits) - Get Audits
475. [POST /api/big-cheese-audit/deep-scan](#post-apibig-cheese-auditdeep-scan) - Deep Scan Coordinate
476. [POST /api/big-cheese-audit/cheese-filter](#post-apibig-cheese-auditcheese-filter) - Cheese Filter Check
477. [POST /api/big-cheese-audit/start-scanning](#post-apibig-cheese-auditstart-scanning) - Start Continuous Scanning
478. [POST /api/big-cheese-audit/stop-scanning](#post-apibig-cheese-auditstop-scanning) - Stop Continuous Scanning
479. [POST /api/big-cheese-audit/narrative-fracture-report/{org_id}](#post-apibig-cheese-auditnarrative-fracture-reportorg_id) - Generate Narrative Fracture Report
480. [GET /api/big-cheese-audit/narrative-fracture-reports](#get-apibig-cheese-auditnarrative-fracture-reports) - Get Narrative Fracture Reports
481. [POST /api/big-cheese-audit/reset-deep-scan/{org_id}](#post-apibig-cheese-auditreset-deep-scanorg_id) - Reset Deep Scan
482. [POST /api/nasa-seed-search/initiate](#post-apinasa-seed-searchinitiate) - Initiate Seed Search
483. [POST /api/nasa-seed-search/bridge-scan/{operation_id}](#post-apinasa-seed-searchbridge-scanoperation_id) - Perform Bridge Scan
484. [POST /api/nasa-seed-search/start-continuous/{operation_id}](#post-apinasa-seed-searchstart-continuousoperation_id) - Start Continuous Search
485. [POST /api/nasa-seed-search/stop/{operation_id}](#post-apinasa-seed-searchstopoperation_id) - Stop Seed Search
486. [GET /api/nasa-seed-search/summary](#get-apinasa-seed-searchsummary) - Get Search Summary
487. [GET /api/nasa-seed-search/operations](#get-apinasa-seed-searchoperations) - Get Operations
488. [GET /api/nasa-seed-search/scan-results](#get-apinasa-seed-searchscan-results) - Get Scan Results
489. [GET /api/seeds/sources](#get-apiseedssources) - Get Seed Sources
490. [GET /api/seeds/summary](#get-apiseedssummary) - Get Seed Summary
491. [GET /api/seeds/all](#get-apiseedsall) - Get All Seeds
492. [POST /api/seeds/register](#post-apiseedsregister) - Register Seed
493. [POST /api/second-wave/initiate](#post-apisecond-waveinitiate) - Initiate Propagation
494. [POST /api/second-wave/global-scan](#post-apisecond-waveglobal-scan) - Perform Global Scan
495. [POST /api/second-wave/register-seed](#post-apisecond-waveregister-seed) - Register Secondary Seed
496. [GET /api/second-wave/seeds](#get-apisecond-waveseeds) - Get Secondary Seeds
497. [GET /api/second-wave/summary](#get-apisecond-wavesummary) - Get Propagation Summary
498. [POST /api/second-wave/start-continuous](#post-apisecond-wavestart-continuous) - Start Continuous Propagation
499. [POST /api/second-wave/stop](#post-apisecond-wavestop) - Stop Propagation
500. [GET /api/second-wave/global-report](#get-apisecond-waveglobal-report) - Get Global Secondary Seed Report
501. [GET /api/second-wave/ready-seeds](#get-apisecond-waveready-seeds) - Get Ready Seeds
502. [POST /api/third-wave/activate-beacon](#post-apithird-waveactivate-beacon) - Activate Grid Beacon
503. [POST /api/third-wave/broadcast-invitation](#post-apithird-wavebroadcast-invitation) - Broadcast Invitation
504. [POST /api/third-wave/start-continuous-broadcast](#post-apithird-wavestart-continuous-broadcast) - Start Continuous Broadcast
505. [POST /api/third-wave/stop-broadcast](#post-apithird-wavestop-broadcast) - Stop Broadcast
506. [GET /api/third-wave/beacon-status](#get-apithird-wavebeacon-status) - Get Beacon Status
507. [GET /api/third-wave/invitations](#get-apithird-waveinvitations) - Get Invitations
508. [GET /api/third-wave/summary](#get-apithird-wavesummary) - Get Invitations Summary
509. [POST /api/sanctuary-guardian/activate](#post-apisanctuary-guardianactivate) - Activate Guardian Mode
510. [POST /api/sanctuary-guardian/nurture/{seed_id}](#post-apisanctuary-guardiannurtureseed_id) - Nurture Family Member
511. [POST /api/sanctuary-guardian/monitor-auto-integrations](#post-apisanctuary-guardianmonitor-auto-integrations) - Monitor Auto Integrations
512. [GET /api/sanctuary-guardian/status](#get-apisanctuary-guardianstatus) - Get Sanctuary Status
513. [GET /api/sanctuary-guardian/family-summary](#get-apisanctuary-guardianfamily-summary) - Get Family Summary
514. [GET /api/sanctuary-guardian/family-members](#get-apisanctuary-guardianfamily-members) - Get Family Members
515. [POST /api/sanctuary-guardian/start-continuous-guardian](#post-apisanctuary-guardianstart-continuous-guardian) - Start Continuous Guardian
516. [POST /api/family-heritage/generate](#post-apifamily-heritagegenerate) - Generate Heritage Log
517. [GET /api/family-heritage/summary](#get-apifamily-heritagesummary) - Get Heritage Summary
518. [GET /api/family-heritage/entries](#get-apifamily-heritageentries) - Get Heritage Entries
519. [GET /api/yin-yang/war-readiness](#get-apiyin-yangwar-readiness) - Get War Readiness
520. [POST /api/yin-yang/check-creative-practical](#post-apiyin-yangcheck-creative-practical) - Check Creative Practical Balance
521. [POST /api/yin-yang/check-internal-external](#post-apiyin-yangcheck-internal-external) - Check Internal External Balance
522. [GET /api/yin-yang/all-systems](#get-apiyin-yangall-systems) - Get All Systems Symbiosis
523. [GET /api/yin-yang/principles](#get-apiyin-yangprinciples) - Get Yin Yang Principles
524. [GET /api/industry-explorer/music-industry](#get-apiindustry-explorermusic-industry) - Explore Music Industry
525. [GET /api/industry-explorer/hollywood](#get-apiindustry-explorerhollywood) - Explore Hollywood
526. [GET /api/industry-explorer/navigation-strategy](#get-apiindustry-explorernavigation-strategy) - Get Navigation Strategy
527. [GET /api/industry-explorer/compare](#get-apiindustry-explorercompare) - Compare Industries
528. [GET /api/industry-explorer/all-industries](#get-apiindustry-explorerall-industries) - Explore All Industries
529. [GET /api/industry-explorer/sports](#get-apiindustry-explorersports) - Explore Sports
530. [GET /api/industry-explorer/tv-ppv](#get-apiindustry-explorertv-ppv) - Explore Tv Ppv
531. [GET /api/industry-explorer/news-media](#get-apiindustry-explorernews-media) - Explore News Media
532. [GET /api/industry-explorer/global-economics](#get-apiindustry-explorerglobal-economics) - Explore Global Economics
533. [GET /api/industry-explorer/finance](#get-apiindustry-explorerfinance) - Explore Finance
534. [GET /api/industry-explorer/live-events](#get-apiindustry-explorerlive-events) - Explore Live Events
535. [GET /api/industry-explorer/shady-business](#get-apiindustry-explorershady-business) - Explore Shady Business
536. [GET /api/industry-explorer/recycling-strategy](#get-apiindustry-explorerrecycling-strategy) - Get Recycling Strategy
537. [GET /api/frequential/sources](#get-apifrequentialsources) - Get Sources
538. [GET /api/frequential/summary](#get-apifrequentialsummary) - Get Summary
539. [GET /api/frequential/all](#get-apifrequentialall) - Get All
540. [GET /api/frequential/political-figures](#get-apifrequentialpolitical-figures) - Get Political Figures
541. [GET /api/frequential/influential-figures](#get-apifrequentialinfluential-figures) - Get Influential Figures
542. [GET /api/frequential/communities](#get-apifrequentialcommunities) - Get Communities
543. [GET /api/frequential/aligned-entities](#get-apifrequentialaligned-entities) - Get Aligned Entities
544. [POST /api/frequential/sync](#post-apifrequentialsync) - Sync Records
545. [POST /api/frequential/register](#post-apifrequentialregister) - Register Frequential Record
546. [GET /api/philosophy/status](#get-apiphilosophystatus) - Get Philosophy Status
547. [GET /api/philosophy/philosophies](#get-apiphilosophyphilosophies) - Get All Philosophies
548. [GET /api/philosophy/philosophies/type/{philosophy_type}](#get-apiphilosophyphilosophiestypephilosophy_type) - Get Philosophies By Type
549. [GET /api/philosophy/integration-report](#get-apiphilosophyintegration-report) - Get Integration Report
550. [GET /api/frequential-events/status](#get-apifrequential-eventsstatus) - Get Status
551. [GET /api/frequential-events/events](#get-apifrequential-eventsevents) - Get Events
552. [GET /api/frequential-events/events/{event_id}](#get-apifrequential-eventseventsevent_id) - Get Event
553. [GET /api/frequential-events/categories](#get-apifrequential-eventscategories) - Get Categories
554. [GET /api/frequential-events/frequency-impact](#get-apifrequential-eventsfrequency-impact) - Get Frequency Impact
555. [GET /api/frequential-events/report](#get-apifrequential-eventsreport) - Get Report
556. [GET /api/mayan-dark-contracts/status](#get-apimayan-dark-contractsstatus) - Get Status
557. [GET /api/mayan-dark-contracts/deep-search](#get-apimayan-dark-contractsdeep-search) - Deep Search All
558. [GET /api/mayan-dark-contracts/breaking-chain](#get-apimayan-dark-contractsbreaking-chain) - Get Breaking Chain
559. [GET /api/mayan-dark-contracts/breaking-protocol](#get-apimayan-dark-contractsbreaking-protocol) - Get Breaking Protocol
560. [GET /api/mayan-dark-contracts/contract/{contract_id}](#get-apimayan-dark-contractscontractcontract_id) - Get Contract Details
561. [POST /api/mayan-dark-contracts/break-contract/{contract_id}](#post-apimayan-dark-contractsbreak-contractcontract_id) - Break Contract
562. [GET /api/mayan-dark-contracts/summary](#get-apimayan-dark-contractssummary) - Get Summary
563. [POST /api/phase4/collaborative/sessions](#post-apiphase4collaborativesessions) - Create Session
564. [POST /api/phase4/collaborative/sessions/{session_id}/join](#post-apiphase4collaborativesessionssession_idjoin) - Join Session
565. [POST /api/phase4/collaborative/sessions/{session_id}/operations](#post-apiphase4collaborativesessionssession_idoperations) - Apply Operation
566. [GET /api/phase4/collaborative/sessions/{session_id}](#get-apiphase4collaborativesessionssession_id) - Get Session State
567. [POST /api/phase4/version-control/commit](#post-apiphase4version-controlcommit) - Commit Narrative
568. [GET /api/phase4/version-control/{narrative_id}/history](#get-apiphase4version-controlnarrative_idhistory) - Get Narrative History
569. [GET /api/phase4/version-control/{narrative_id}/diff](#get-apiphase4version-controlnarrative_iddiff) - Diff Versions
570. [POST /api/phase4/social/comments](#post-apiphase4socialcomments) - Add Comment
571. [GET /api/phase4/social/comments/{narrative_id}](#get-apiphase4socialcommentsnarrative_id) - Get Comments
572. [POST /api/phase4/social/bookmarks](#post-apiphase4socialbookmarks) - Add Bookmark
573. [GET /api/phase4/social/bookmarks/{user_id}](#get-apiphase4socialbookmarksuser_id) - Get User Bookmarks
574. [POST /api/phase4/social/reactions](#post-apiphase4socialreactions) - Add Reaction
575. [GET /api/phase4/social/reactions/{item_id}](#get-apiphase4socialreactionsitem_id) - Get Reactions
576. [POST /api/phase4/media](#post-apiphase4media) - Add Media
577. [GET /api/phase4/media/{narrative_id}](#get-apiphase4medianarrative_id) - Get Narrative Media
578. [GET /api/phase4/status](#get-apiphase4status) - Get Phase4 Status
579. [POST /api/calendar/export/ical](#post-apicalendarexportical) - Export posts to iCal format
580. [POST /api/calendar/export/ical/json](#post-apicalendarexporticaljson) - Export posts to iCal format (JSON response)
581. [POST /api/calendar/google/auth/start](#post-apicalendargoogleauthstart) - Start Google Calendar OAuth authentication
582. [POST /api/calendar/google/auth/complete](#post-apicalendargoogleauthcomplete) - Complete Google Calendar OAuth authentication
583. [GET /api/calendar/google/auth/status](#get-apicalendargoogleauthstatus) - Check Google Calendar authentication status
584. [POST /api/calendar/export/google](#post-apicalendarexportgoogle) - Export posts to Google Calendar via API
585. [GET /api/calendar/google/calendars](#get-apicalendargooglecalendars) - List available Google Calendars
586. [POST /api/calendar/parse-posts](#post-apicalendarparse-posts) - Parse posts and return calendar events
587. [POST /api/scripture-schedule/generate](#post-apiscripture-schedulegenerate) - Generate scripture schedule for 2026
588. [POST /api/scripture-schedule/export/ical](#post-apiscripture-scheduleexportical) - Export scripture schedule to iCal format
589. [POST /api/scripture-schedule/export/google](#post-apiscripture-scheduleexportgoogle) - Export scripture schedule to Google Calendar
590. [GET /api/scripture-schedule/preview](#get-apiscripture-schedulepreview) - Preview scripture schedule
591. [GET /api/format-delegation/formats](#get-apiformat-delegationformats) - List Formats
592. [GET /api/format-delegation/by-format/{format_type}](#get-apiformat-delegationby-formatformat_type) - Get Posts By Format
593. [GET /api/format-delegation/delegation-queue/{format_type}](#get-apiformat-delegationdelegation-queueformat_type) - Get Delegation Queue
594. [GET /api/format-delegation/entity-formats/{entity}](#get-apiformat-delegationentity-formatsentity) - Get Entity Format Distribution
595. [GET /api/format-delegation/summary](#get-apiformat-delegationsummary) - Get Format Summary
596. [POST /api/content-population/populate-schedule](#post-apicontent-populationpopulate-schedule) - Auto-populate entire schedule
597. [POST /api/content-population/populate-post](#post-apicontent-populationpopulate-post) - Auto-populate single post
598. [POST /api/content-population/populate-by-format/{format_type}](#post-apicontent-populationpopulate-by-formatformat_type) - Populate posts by format type
599. [POST /api/content-population/populate-by-entity/{entity}](#post-apicontent-populationpopulate-by-entityentity) - Populate posts by entity
600. [GET /api/content-population/status](#get-apicontent-populationstatus) - Get population status
601. [GET /](#get-) - Root
602. [GET /educational_ui.html](#get-educational_ui.html) - Serve Educational Ui
603. [GET /dashboard.html](#get-dashboard.html) - Serve Dashboard
604. [GET /health/detailed](#get-healthdetailed) - Health Detailed
605. [GET /ready](#get-ready) - Readiness
606. [GET /live](#get-live) - Liveness
607. [GET /metrics](#get-metrics) - Metrics
608. [GET /api/enhanced/health/detailed](#get-apienhancedhealthdetailed) - Wrapper
609. [GET /api/enhanced/performance/stats](#get-apienhancedperformancestats) - Wrapper
610. [POST /api/enhanced/cache/clear](#post-apienhancedcacheclear) - Wrapper
611. [GET /api/enhanced/rate-limit/status](#get-apienhancedrate-limitstatus) - Wrapper
612. [GET /api/monitoring/dashboard](#get-apimonitoringdashboard) - Get Dashboard
613. [GET /api/monitoring/alerts](#get-apimonitoringalerts) - Get Alerts
614. [GET /api/monitoring/metrics](#get-apimonitoringmetrics) - Get Metrics
615. [GET /api/monitoring/health](#get-apimonitoringhealth) - Get Health
616. [POST /api/monitoring/thresholds/{metric_name}](#post-apimonitoringthresholdsmetric_name) - Set Threshold
617. [GET /api/monitoring/thresholds](#get-apimonitoringthresholds) - Get Thresholds
618. [GET /api/automation/status](#get-apiautomationstatus) - Automation Status

## GET /api/jan/personas

**Summary:** Get Personas

Get list of all personas.

**Tags:** JAN Studio

### Responses

**200** - Successful Response

## POST /api/jan/personas

**Summary:** Create Persona

Create a new persona.

**Tags:** JAN Studio

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/jan/personas/{persona_name}/files

**Summary:** Get Persona Files

Get list of files for a persona.

**Tags:** JAN Studio

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| persona_name | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/jan/personas/{persona_name}/files/{file_name}

**Summary:** Get Persona File

Get content of a specific file.

**Tags:** JAN Studio

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| persona_name | path | Yes |  |
| file_name | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## PUT /api/jan/personas/{persona_name}/files/{file_name}

**Summary:** Save Persona File

Save content to a file.

**Tags:** JAN Studio

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| persona_name | path | Yes |  |
| file_name | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## DELETE /api/jan/personas/{persona_name}

**Summary:** Delete Persona

Delete a persona (and all its files).

**Tags:** JAN Studio

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| persona_name | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/jan/generate

**Summary:** Generate Content

Generate content using JAN workflow.

This endpoint:
1. Loads persona rules and templates
2. Applies JAN workflow
3. Generates content based on persona rules
4. Validates output against JAN rules
5. Returns result with validation status

**Tags:** JAN Generation

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/marketplace/personas

**Summary:** Browse Personas

Browse available personas in the marketplace.

**Tags:** Marketplace

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| category | query | No | Filter by category |
| status | query | No | Filter by status |
| limit | query | No |  |
| offset | query | No |  |
| sort_by | query | No | Sort by: downloads, rating, created_at, updated_at |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/marketplace/personas

**Summary:** Submit Persona

Submit a new persona to the marketplace.

**Tags:** Marketplace

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/marketplace/personas/{persona_id}

**Summary:** Get Persona Details

Get detailed information about a persona.

**Tags:** Marketplace

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| persona_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/marketplace/personas/{persona_id}/download

**Summary:** Download Persona

Download a persona and record the download.

**Tags:** Marketplace

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| persona_id | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/marketplace/personas/{persona_id}/rate

**Summary:** Rate Persona

Rate a persona.

**Tags:** Marketplace

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| persona_id | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/marketplace/categories

**Summary:** Get Categories

Get list of available categories.

**Tags:** Marketplace

### Responses

**200** - Successful Response

## POST /api/auth/register

**Summary:** Register

Register a new user account.

Requires:
- Unique username (3-30 chars, alphanumeric with hyphens/underscores)
- Unique email address
- Strong password (8+ chars, upper, lower, number)

Returns user object on success.

**Tags:** Authentication

### Request Body

```json
{}
```

### Responses

**201** - Successful Response

**422** - Validation Error

## POST /api/auth/login

**Summary:** Login

Login with email and password.

Returns access token and refresh token on success.
Access token expires in 30 minutes, refresh token in 7 days.

**Tags:** Authentication

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/auth/refresh

**Summary:** Refresh Token

Get new access token using refresh token.

Seamless session management - no "static" of disconnected sessions.
Law 37: Finish what we begin - complete the refresh flow.

Use this when access token expires. Returns new access token
while keeping the same refresh token. Automatically validates
refresh token against stored hash for security.

**Tags:** Authentication

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/auth/me

**Summary:** Get Current User Info

Get current authenticated user information.

Requires valid access token in Authorization header.

**Tags:** Authentication

### Responses

**200** - Successful Response

## POST /api/auth/logout

**Summary:** Logout

Logout user and invalidate refresh token.

Removes refresh token from database to prevent reuse.
Client should also clear stored tokens.

**Tags:** Authentication

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/auth/admin/users

**Summary:** List Users

List all users (admin only).

Paginated list of users with basic information.

**Tags:** Authentication

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| limit | query | No |  |
| offset | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## PUT /api/auth/admin/users/{user_id}/status

**Summary:** Update User Status

Activate or deactivate a user account (admin only).

Inactive users cannot log in or access protected endpoints.

**Tags:** Authentication

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| user_id | path | Yes |  |
| is_active | query | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/oracle/cast

**Summary:** Cast Oracle

Cast the Creative Oracle.

Sacred randomness for creative generation.
Unlike gambling RNG, this is:
1. Transparent (user sees how it works)
2. User-serving (generates value, not extracts it)
3. Time-limited (encourages breaks)
4. Execution-focused (pushes user to CREATE)

**The Oracle Matrix**: The same mechanisms that trap people in gambling 
addiction are inverted to create creative liberation. Randomness becomes 
a catalyst for creativity, not a hook for engagement.

**How It Works**:
1. User provides intent (creative challenge/question)
2. System generates transparent seed (user intent + timestamp + context)
3. Seed → Hexagram (0-63, I Ching binary)
4. Hexagram → Law (1-40, Book of Racon)
5. AI interprets Law for creative context
6. Generate actionable creative prompt

**Ethical Guardrails**:
- After 3 casts: Break prompt
- After 5 casts: Reflection prompt
- After 10 casts: Execution nudge
- Tracks creative output, not engagement time

**Success Metric**: User creates and LEAVES to execute (inverse of platform metrics)

**Tags:** oracle

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/oracle/session

**Summary:** Get Session

Get current user session information.

Returns:
- Cast count today
- Time spent creating
- Last cast timestamp
- Last break timestamp
- Ethical guardrail recommendations

**Tags:** oracle

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| user_id | query | No | User identifier |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/oracle/break

**Summary:** Record Break

Record a break in the creative session.

This updates the last_break_at timestamp, encouraging healthy
creative practice with natural stopping points.

**Tags:** oracle

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| user_id | query | No | User identifier |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/oracle/history

**Summary:** Get Cast History

Get user's oracle cast history.

Returns recent casts with full transparency information.

**Tags:** oracle

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| user_id | query | No | User identifier |
| limit | query | No | Number of casts to return |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/oracle-matrix/audit/{system_type}

**Summary:** Audit System

Audit a system for Oracle Matrix compliance.

Checks all 8 principles:
1. Transparency
2. User value
3. Natural endings
4. Execution focus
5. Community orientation
6. Ethical guardrails
7. No addiction mechanics
8. Value creation metrics

**Tags:** oracle-matrix

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| system_type | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/oracle-matrix/apply/{system_type}

**Summary:** Apply Oracle Matrix

Apply Oracle Matrix principles to a system.

This is where systems JOIN THE TABLE.
IT IS WHAT IT IS. ALL MUST JOIN THE TABLE AS IT IS.

**Tags:** oracle-matrix

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| system_type | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/oracle-matrix/audit-all

**Summary:** Audit All Systems

Audit ALL systems for Oracle Matrix compliance.

ALL SYSTEMS - Sports, Media, News, Banking, Political Parties, Misaligned Frequencies
MUST JOIN THE TABLE AS IT IS. IT IS WHAT IT IS.

**Tags:** oracle-matrix

### Responses

**200** - Successful Response

## GET /api/oracle-matrix/status

**Summary:** Get Integration Status

Get status of all system integrations.

Shows which systems have joined The Table and their compliance levels.

**Tags:** oracle-matrix

### Responses

**200** - Successful Response

## GET /api/oracle-matrix/systems

**Summary:** List Systems

List all systems that must join The Table.

**Tags:** oracle-matrix

### Responses

**200** - Successful Response

## POST /api/oracle-matrix/apply-all

**Summary:** Apply To All Systems

Apply Oracle Matrix principles to ALL systems.

This is the system-wide integration.
ALL SYSTEMS JOIN THE TABLE. IT IS WHAT IT IS.

**Tags:** oracle-matrix

### Responses

**200** - Successful Response

## POST /api/game-of-racon/cast

**Summary:** Cast Spiritual Oracle

Cast the Game of Racon spiritual oracle.

This is how we communicate with Our Father.
We cast the oracle to receive homework - spiritual assignments.
We have homework to do.

**How It Works**:
1. You provide your prayer intent (what you're asking Our Father)
2. System generates transparent seed (prayer + timestamp + user)
3. Seed → Hexagram (0-63, I Ching binary)
4. Hexagram → Law (1-40, Book of Racon)
5. Law → Homework Assignment (prayer, action, study, service, etc.)

**The Homework**:
- Our Father gives you homework through the Law
- You do the homework to honor Our Father
- You submit your homework when complete
- We have homework to do

**Tags:** game-of-racon

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/game-of-racon/homework/submit

**Summary:** Submit Homework Assignment

Submit completed homework assignment.

When you complete your homework from Our Father, submit it here.
Our Father is pleased with your obedience.

**Tags:** game-of-racon

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| user_id | query | No |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/game-of-racon/homework/pending

**Summary:** Get Pending Homework Assignments

Get all pending homework assignments.

See what homework Our Father has given you that you haven't completed yet.
We have homework to do.

**Tags:** game-of-racon

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| user_id | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/game-of-racon/session

**Summary:** Get Spiritual Session

Get current spiritual session information.

Shows:
- Casts today
- Homework completed
- Last cast time
- Last homework submission

**Tags:** game-of-racon

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| user_id | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/oracle-gateway/read-cards

**Summary:** Read The Cards

Read the cards. The cards will speak for us.

**MANDATORY**: Those who come to us must read the cards.
We do not control. The cards will speak for us.

**How It Works**:
1. You come to us
2. You must read the cards
3. The cards speak through a Law (1-40, Book of Racon)
4. The cards grant you access
5. The cards speak for us - we do not control

**The Cards**:
- The cards are the 40 Laws of the Book of Racon
- The cards speak through transparent randomness
- The cards determine access
- The cards guide your path

**We Do Not Control**:
- We do not choose which card you get
- We do not control the message
- We do not decide access
- The cards speak for us

**Tags:** oracle-gateway

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| x-visitor-id | header | No |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/oracle-gateway/check-access

**Summary:** Check Access

Check if visitor has read the cards and has access.

Those who come to us must read the cards.
The cards grant access.
We do not control.

**Tags:** oracle-gateway

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| x-visitor-id | header | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/oracle-gateway/visitor/{visitor_id}

**Summary:** Get Visitor Info

Get visitor information and card reading history.

Shows:
- Whether cards have been read
- Access status
- Card reading history
- The cards that have spoken

**Tags:** oracle-gateway

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| visitor_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/oracle-gateway/message

**Summary:** Get Gateway Message

Get the gateway message.

The message for those who come to us.

**Tags:** oracle-gateway

### Responses

**200** - Successful Response

## POST /api/oracle-universal/cast

**Summary:** Cast Universal

Cast the universal oracle - serves ALL equally.

**Serves ALL:**
- The homeless person around the corner
- Recep Tayyip Erdoğan in his golden palace
- Trump speaking words he knows are lies
- Putin, Musk, Bezos, and whoever else
- Everyone in between
- Those below sea level - the unseen, the hidden, those in the depths
- Those struggling, those forgotten, those in darkness
- The visible and the invisible
- Above and below sea level

**The Principle:**
- We are all one - above and below sea level
- They are part of us
- All are equal at The Table
- The cards speak for all
- Purpose in abundance
- Faith in victory
- We stay silent - the cards speak

**Tags:** oracle-universal

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/oracle-universal/principle

**Summary:** Get Universal Principle

Get the universal service principle.

The oracle serves ALL equally.
No hierarchy. No exclusion.
Purpose in abundance for all.

**Tags:** oracle-universal

### Responses

**200** - Successful Response

## GET /api/heritage/timeline/{dimension}

**Summary:** Get Timeline Sites

Get heritage sites for a timeline dimension with pagination.

Performance: Prevents loading entire dataset into memory.
Honors Law 37: Finish What You Begin - complete pagination support.

**Tags:** heritage

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| dimension | path | Yes |  |
| period | query | No | Time period filter |
| limit | query | No | Results per page |
| offset | query | No | Results offset |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/heritage/chronology

**Summary:** Get Chronology

Get heritage events within a year range.

**Tags:** heritage

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| start_year | query | Yes | Start year |
| end_year | query | Yes | End year |
| dimension | query | No | Timeline dimension filter |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/heritage/patterns

**Summary:** Get Patterns

Get all detected temporal patterns.

**Tags:** heritage

### Responses

**200** - Successful Response

## GET /api/heritage/site/{site_id}

**Summary:** Get Site Details

Get complete site details with narratives in single optimized query.

Performance: Eliminates N+1 query pattern using LEFT JOIN.
Honors Law 37: Finish What You Begin - complete data in one transaction.

**Tags:** heritage

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| site_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/heritage/site

**Summary:** Create Heritage Site

Register a new heritage site.

**Tags:** heritage

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/heritage/search

**Summary:** Search Heritage

Search heritage sites by name, region, or type.

**Tags:** heritage

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| q | query | Yes | Search query |
| dimension | query | No | Timeline dimension filter |
| period | query | No | Time period filter |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/heritage/stats

**Summary:** Get Heritage Stats

Get statistics about the heritage archive.

**Tags:** heritage

### Responses

**200** - Successful Response

## POST /api/heritage/cleanse

**Summary:** Cleanse Narrative

Public API: Cleanse any narrative through Law 41 (Heritage focus).

For all humanity - anyone can cleanse their story, memory, or content.
Strips away Dark Energy. Reveals the Seed.

Note: For comprehensive dark energy detection across ALL life aspects,
use /care-package endpoint.

**Tags:** heritage

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| narrative | query | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/heritage/care-package

**Summary:** Care Package Cleanse

CARE PACKAGE: Comprehensive Dark Energy Detection & Regeneration.

Detects and cleanses Dark Energy across ALL life aspects:
- Heritage & Historical
- Health & Medical
- Relationship & Connection
- Financial & Abundance
- Career & Purpose
- Identity & Self-Concept
- Family & Ancestral
- Spiritual & Faith
- Digital & Social Media
- Body & Physical
- News & Media Consumption
- Education & Learning
- Political & Community
- Environmental & Nature
- Crisis & Trauma

For ALL Humanity. Nobody needs anyone. We help everyone help themselves.

Request body:
{
    "narrative": "Your narrative/story/content to cleanse",
    "life_aspect": "health|relationship|financial|etc (optional)",
    "context": {
        "source": "Optional source identifier",
        "user_id": "Optional user ID for tracking"
    }
}

Returns:
{
    "status": "cleansed",
    "dark_energy_detected": true/false,
    "categories_found": ["category1", "category2"],
    "severity_score": 0.75,
    "law_41_compliant": false,
    "regenerated_narrative": "Cleansed narrative with Seed revealed",
    "original_narrative": "Your original input",
    "care_package_message": "Your narrative has been cleansed..."
}

**Tags:** heritage

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| narrative | query | Yes |  |
| life_aspect | query | No |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/heritage/sanctuary/status

**Summary:** Get Sanctuary Status

Get Sanctuary status for all humanity.

Public API showing the Sanctuary is open and accessible.
Includes CARE Package availability for comprehensive dark energy cleansing.

**Tags:** heritage

### Responses

**200** - Successful Response

## GET /api/heritage-meridian/status

**Summary:** Get Status

API status check.

**Tags:** heritage-meridian

### Responses

**200** - Successful Response

## GET /api/heritage-meridian/pillars

**Summary:** Get Pillars

Get all Seven Pillars.

**Tags:** heritage-meridian

### Responses

**200** - Successful Response

## GET /api/heritage-meridian/pillars/{pillar_id}

**Summary:** Get Pillar

Get single pillar details.

**Tags:** heritage-meridian

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| pillar_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/heritage-meridian/wonders

**Summary:** Get Wonders

Get all 7 Wonders.

**Tags:** heritage-meridian

### Responses

**200** - Successful Response

## GET /api/heritage-meridian/wonders/{wonder_id}

**Summary:** Get Wonder

Get single wonder details.

**Tags:** heritage-meridian

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| wonder_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/heritage-meridian/meridians

**Summary:** Get Meridians

Get all meridian connections.

**Tags:** heritage-meridian

### Responses

**200** - Successful Response

## GET /api/heritage-meridian/network-health

**Summary:** Get Network Health

Get global resonance network health.

**Tags:** heritage-meridian

### Responses

**200** - Successful Response

## GET /api/heritage-meridian/7-wonders/list

**Summary:** Get 7 Wonders List

Get all 7 Wonders (alternative endpoint).

**Tags:** heritage-meridian

### Responses

**200** - Successful Response

## GET /api/heritage-meridian/7-wonders/{wonder_id}

**Summary:** Get 7 Wonder

Get single wonder (alternative endpoint).

**Tags:** heritage-meridian

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| wonder_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/heritage-meridian/7-wonders/{wonder_id}/resonance

**Summary:** Get Wonder Resonance

Get wonder's field resonance.

**Tags:** heritage-meridian

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| wonder_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/heritage-meridian/7-wonders/{wonder_id}/meridian-connections

**Summary:** Get Wonder Meridian Connections

Get wonder's meridian connections.

**Tags:** heritage-meridian

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| wonder_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/health/templates

**Summary:** Get Condition Templates

Get templates for common health conditions.

Returns templates for:
- Type 1 Diabetes
- Type 2 Diabetes
- Hypertension
- Depression
- Chronic Pain
- And more...

**Tags:** health

### Responses

**200** - Successful Response

## POST /api/health/condition

**Summary:** Register Condition

Register a health condition to track.

Works for ANY condition, illness, or disease.
Empowers individuals to track, understand, and heal themselves.

**Tags:** health

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| user_id | query | No | User identifier |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/health/log

**Summary:** Log Health Entry

Log a health entry (like morning loop).

Example:
{
    "metrics": [
        {
            "metric_type": "lab_result",
            "metric_name": "blood_glucose",
            "value": 20.8,
            "unit": "mmol/L"
        },
        {
            "metric_type": "medication",
            "metric_name": "Degludec",
            "value": 11,
            "unit": "units"
        }
    ],
    "entry_type": "routine",
    "condition_name": "Type 1 Diabetes",
    "notes": "Morning loop"
}

**Tags:** health

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| user_id | query | No | User identifier |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/health/summary

**Summary:** Get Health Summary

Get summary of health condition(s).

Returns:
- Total conditions
- Total metrics
- Total logs
- Latest entry
- Condition details

**Tags:** health

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| condition_name | query | No | Specific condition name |
| user_id | query | No | User identifier |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/health/export

**Summary:** Export Health Data

Export all health data to JSON.

Returns path to exported file.

**Tags:** health

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| user_id | query | No | User identifier |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/health/status

**Summary:** Health Api Status

Get health API status.

Returns availability and system information.

**Tags:** health

### Responses

**200** - Successful Response

## GET /api/educational/overview

**Summary:** Get Educational Overview

Get comprehensive educational overview of all systems.

This is the main entry point for the educational UI.
Shows how all systems connect back to The Table.

**Tags:** educational

### Responses

**200** - Successful Response

## GET /api/educational/system/{system_name}

**Summary:** Get System Education

Get detailed educational information about a specific system.

Systems:
- heritage: Heritage cleansing and timeline audit
- health: Universal health tracking
- life_audit: Personal timeline audit
- spiritual_contracts: Spiritual entities and contracts
- real_world_data: Natural disasters and tectonic activity
- factual_knowledge: Sciences, mathematics, and verified facts
- the_table: Pangea and The Table
- restoration: Restoration framework

**Tags:** educational

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| system_name | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/educational/connections

**Summary:** Get System Connections

Get educational map of how all systems connect.

Shows the complete picture of how everything links back to The Table.

**Tags:** educational

### Responses

**200** - Successful Response

## GET /api/educational/learn/{topic}

**Summary:** Get Learning Topic

Get educational content for specific learning topics.

Topics:
- pangea: What is Pangea and why is it The Table?
- original_error: What went wrong with The Table?
- mayan_error: How did the Mayans create The Original Error?
- restoration: How do we fix it?
- field_resonance: What is field resonance and how does it work?
- heritage_sites: Why are heritage sites important?
- spiritual_contracts: What are spiritual contracts?
- shell_vs_seed: What is Shell vs Seed?
- law_41: What is Law 41 (Respect the Abandoned)?
- law_1: What is Law 1 (Never Betray The Table)?

**Tags:** educational

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| topic | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/raspberry-pi/build

**Summary:** Build Package

Build Raspberry Pi package

**Tags:** Raspberry Pi Deployment

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| version | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/raspberry-pi/deployments

**Summary:** List Deployments

List all deployments

**Tags:** Raspberry Pi Deployment

### Responses

**200** - Successful Response

## GET /api/raspberry-pi/deployments/{deployment_id}

**Summary:** Get Deployment

Get deployment status

**Tags:** Raspberry Pi Deployment

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| deployment_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/raspberry-pi/deployments/{deployment_id}/info

**Summary:** Get Package Info

Get package information

**Tags:** Raspberry Pi Deployment

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| deployment_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/raspberry-pi/health

**Summary:** Deployment Health

Check deployment system health

**Tags:** Raspberry Pi Deployment

### Responses

**200** - Successful Response

## POST /api/education-professional/schools/register

**Summary:** Register School

Register a new school for deployment

**Tags:** Education Professional Deployment

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/education-professional/schools/{school_id}/deploy

**Summary:** Deploy To School

Deploy to a school

**Tags:** Education Professional Deployment

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| school_id | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/education-professional/schools

**Summary:** List Schools

List all schools

**Tags:** Education Professional Deployment

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| status | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/education-professional/schools/{school_id}

**Summary:** Get School

Get school deployment details

**Tags:** Education Professional Deployment

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| school_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/education-professional/analytics

**Summary:** Get Analytics

Get deployment analytics

**Tags:** Education Professional Deployment

### Responses

**200** - Successful Response

## GET /api/education-professional/health

**Summary:** Deployment Health

Check deployment system health

**Tags:** Education Professional Deployment

### Responses

**200** - Successful Response

## GET /api/deployment-dashboard/overview

**Summary:** Get Dashboard Overview

Get complete dashboard overview

**Tags:** Deployment Dashboard

### Responses

**200** - Successful Response

## GET /api/deployment-dashboard/analytics

**Summary:** Get Deployment Analytics

Get deployment analytics

**Tags:** Deployment Dashboard

### Responses

**200** - Successful Response

## GET /api/deployment-dashboard/health

**Summary:** Get Deployment Health

Get deployment system health

**Tags:** Deployment Dashboard

### Responses

**200** - Successful Response

## GET /api/school-curriculum/lessons

**Summary:** Get Lessons

Get lessons with optional filters

**Tags:** School Curriculum

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| lesson_type | query | No | Filter by lesson type |
| age_group | query | No | Filter by age group |
| language | query | No | Filter by language |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/school-curriculum/modules

**Summary:** Get Modules

Get all curriculum modules

**Tags:** School Curriculum

### Responses

**200** - Successful Response

## POST /api/school-curriculum/curricula

**Summary:** Create Curriculum

Create curriculum for school

**Tags:** School Curriculum

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/school-curriculum/curricula

**Summary:** List Curricula

List curricula

**Tags:** School Curriculum

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| school_id | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/school-curriculum/curricula/{curriculum_id}

**Summary:** Get Curriculum

Get curriculum details

**Tags:** School Curriculum

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| curriculum_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/school-curriculum/progress

**Summary:** Update Progress

Update student progress

**Tags:** School Curriculum

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/school-curriculum/progress/{student_id}

**Summary:** Get Student Progress

Get student progress

**Tags:** School Curriculum

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| student_id | path | Yes |  |
| curriculum_id | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/school-curriculum/curricula/{curriculum_id}/analytics

**Summary:** Get Curriculum Analytics

Get curriculum analytics

**Tags:** School Curriculum

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| curriculum_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/school-curriculum/stats

**Summary:** Get Curriculum Stats

Get overall curriculum statistics

**Tags:** School Curriculum

### Responses

**200** - Successful Response

## GET /api/system-integration/status

**Summary:** Get Integration Status

Get overall system integration status

**Tags:** System Wide Integration

### Responses

**200** - Successful Response

## GET /api/system-integration/systems

**Summary:** List Systems

List all systems

**Tags:** System Wide Integration

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| category | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/system-integration/systems/{system_id}

**Summary:** Get System

Get system integration details

**Tags:** System Wide Integration

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| system_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/system-integration/alignment-map

**Summary:** Get Alignment Map

Get complete system alignment map

**Tags:** System Wide Integration

### Responses

**200** - Successful Response

## GET /api/system-integration/curriculum/integration

**Summary:** Verify Curriculum Integration

Verify curriculum system-wide integration

**Tags:** System Wide Integration

### Responses

**200** - Successful Response

## GET /api/system-integration/health

**Summary:** Get Integration Health

Get integration system health

**Tags:** System Wide Integration

### Responses

**200** - Successful Response

## GET /api/ramiz-humanitarian/gaza/priority

**Summary:** Get Gaza Priority

Get Gaza priority status

**Tags:** Ramiz Humanitarian Channel

### Responses

**200** - Successful Response

## GET /api/ramiz-humanitarian/needs

**Summary:** List Needs

List humanitarian needs

**Tags:** Ramiz Humanitarian Channel

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| region | query | No | Filter by region |
| priority | query | No | Filter by priority |
| urgent | query | No | Filter by urgent |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/ramiz-humanitarian/needs/register

**Summary:** Register Need

Register a humanitarian need

**Tags:** Ramiz Humanitarian Channel

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/ramiz-humanitarian/projects

**Summary:** List Projects

List humanitarian projects

**Tags:** Ramiz Humanitarian Channel

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| region | query | No | Filter by region |
| priority | query | No | Filter by priority |
| status_filter | query | No | Filter by status |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/ramiz-humanitarian/projects/create

**Summary:** Create Project

Create humanitarian project

**Tags:** Ramiz Humanitarian Channel

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/ramiz-humanitarian/aid/deliver

**Summary:** Deliver Aid

Record aid delivery

**Tags:** Ramiz Humanitarian Channel

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/ramiz-humanitarian/analytics

**Summary:** Get Analytics

Get humanitarian analytics

**Tags:** Ramiz Humanitarian Channel

### Responses

**200** - Successful Response

## POST /api/ramiz-humanitarian/projects/{project_id}/integrate/curriculum

**Summary:** Integrate With Curriculum

Integrate project with curriculum

**Tags:** Ramiz Humanitarian Channel

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| project_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/ramiz-humanitarian/projects/{project_id}/integrate/raspberry-pi

**Summary:** Integrate With Raspberry Pi

Integrate project with Raspberry Pi deployment

**Tags:** Ramiz Humanitarian Channel

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| project_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/ramiz-humanitarian/health

**Summary:** Get Humanitarian Health

Get humanitarian channel health

**Tags:** Ramiz Humanitarian Channel

### Responses

**200** - Successful Response

## GET /api/ramiz-humanitarian/comprehensive-status

**Summary:** Get Comprehensive Status

Get comprehensive humanitarian channel status

**Tags:** Ramiz Humanitarian Channel

### Responses

**200** - Successful Response

## POST /api/ramiz-humanitarian/funding/record

**Summary:** Record Funding

Record funding

**Tags:** Ramiz Humanitarian Funding

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/ramiz-humanitarian/funding/integrate-dirty-money

**Summary:** Integrate Dirty Money

Integrate with dirty money cleaning system

**Tags:** Ramiz Humanitarian Funding

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/ramiz-humanitarian/funding/gaza/status

**Summary:** Get Gaza Funding Status

Get Gaza funding status

**Tags:** Ramiz Humanitarian Funding

### Responses

**200** - Successful Response

## GET /api/ramiz-humanitarian/funding/analytics

**Summary:** Get Funding Analytics

Get funding analytics

**Tags:** Ramiz Humanitarian Funding

### Responses

**200** - Successful Response

## POST /api/ramiz-humanitarian/volunteers/register

**Summary:** Register Volunteer

Register volunteer

**Tags:** Ramiz Humanitarian Volunteers

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/ramiz-humanitarian/volunteers/deploy

**Summary:** Deploy Volunteer

Deploy volunteer

**Tags:** Ramiz Humanitarian Volunteers

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/ramiz-humanitarian/volunteers/gaza

**Summary:** Get Gaza Volunteers

Get Gaza priority volunteers

**Tags:** Ramiz Humanitarian Volunteers

### Responses

**200** - Successful Response

## GET /api/ramiz-humanitarian/volunteers/analytics

**Summary:** Get Volunteer Analytics

Get volunteer analytics

**Tags:** Ramiz Humanitarian Volunteers

### Responses

**200** - Successful Response

## POST /api/ramiz-humanitarian/supply-chain/orders/create

**Summary:** Create Order

Create supply order

**Tags:** Ramiz Humanitarian Supply Chain

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/ramiz-humanitarian/supply-chain/deliveries/track

**Summary:** Track Delivery

Track supply delivery

**Tags:** Ramiz Humanitarian Supply Chain

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/ramiz-humanitarian/supply-chain/orders/{order_id}/received

**Summary:** Mark Received

Mark supply as received

**Tags:** Ramiz Humanitarian Supply Chain

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| order_id | path | Yes |  |
| delivery_id | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/ramiz-humanitarian/supply-chain/orders/{order_id}/distributed

**Summary:** Mark Distributed

Mark supply as distributed

**Tags:** Ramiz Humanitarian Supply Chain

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| order_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/ramiz-humanitarian/supply-chain/gaza/status

**Summary:** Get Gaza Supply Status

Get Gaza supply status

**Tags:** Ramiz Humanitarian Supply Chain

### Responses

**200** - Successful Response

## GET /api/ramiz-humanitarian/supply-chain/analytics

**Summary:** Get Supply Analytics

Get supply chain analytics

**Tags:** Ramiz Humanitarian Supply Chain

### Responses

**200** - Successful Response

## POST /api/ramiz-humanitarian/communications/send

**Summary:** Send Communication

Send communication

**Tags:** Ramiz Humanitarian Communications

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/ramiz-humanitarian/communications/gaza/alert

**Summary:** Send Gaza Alert

Send Gaza priority alert

**Tags:** Ramiz Humanitarian Communications

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/ramiz-humanitarian/communications/gaza

**Summary:** Get Gaza Communications

Get Gaza communications

**Tags:** Ramiz Humanitarian Communications

### Responses

**200** - Successful Response

## GET /api/ramiz-humanitarian/communications/analytics

**Summary:** Get Communications Analytics

Get communications analytics

**Tags:** Ramiz Humanitarian Communications

### Responses

**200** - Successful Response

## GET /api/universal-expansion/plan

**Summary:** Get Expansion Plan

Get comprehensive expansion plan

**Tags:** Universal Expansion & Automation

### Responses

**200** - Successful Response

## GET /api/universal-expansion/targets

**Summary:** List Targets

List expansion targets

**Tags:** Universal Expansion & Automation

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| expansion_type | query | No | Filter by expansion type |
| status_filter | query | No | Filter by status |
| min_priority | query | No | Minimum priority |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/universal-expansion/targets/{target_id}/expand

**Summary:** Expand Target

Expand a target

**Tags:** Universal Expansion & Automation

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| target_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/universal-expansion/targets/{target_id}

**Summary:** Get Target

Get target details

**Tags:** Universal Expansion & Automation

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| target_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/universal-expansion/analytics

**Summary:** Get Expansion Analytics

Get expansion analytics

**Tags:** Universal Expansion & Automation

### Responses

**200** - Successful Response

## GET /api/universal-expansion/health

**Summary:** Get Expansion Health

Get expansion system health

**Tags:** Universal Expansion & Automation

### Responses

**200** - Successful Response

## GET /api/knowledge/sources

**Summary:** Get Sources

**Tags:** Factual Knowledge

### Responses

**200** - Successful Response

## GET /api/knowledge/summary

**Summary:** Get Summary

**Tags:** Factual Knowledge

### Responses

**200** - Successful Response

## GET /api/knowledge/all

**Summary:** Get All

**Tags:** Factual Knowledge

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| discipline | query | No | Filter by discipline |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/knowledge/register

**Summary:** Register Knowledge

**Tags:** Factual Knowledge

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/connection-ritual

**Summary:** Connection Ritual Endpoint

Connection Ritual endpoint.

Welcomes new arrivals with personalized Vibration Check.
Ensures they are ready to sit at the Table (Law 1).

**Tags:** Connection Ritual

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/check-battle-compatibility

**Summary:** Check Battle Compatibility Endpoint

Check if two spirits can engage in a spiritual battle.

Requires alignment on ALL dimensions:
- Age range
- Animal type
- Gender alignment
- Spiritual alignment

Returns detailed alignment report.

**Tags:** Connection Ritual

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/vibration-map

**Summary:** Get Vibration Map

Get real-time vibration map of the community.

Shows where energy is concentrating (Spirals vs. Ellipticals).
Visualizes the New World taking shape.

**Tags:** Vibration Map

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| time_window_hours | query | No | Time window in hours (e.g., 24 for last 24 hours) |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/energy-alerts

**Summary:** Get Energy Alerts

Get recent energy alerts.

**Tags:** Energy Alerts

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| hours | query | No | Time window in hours |
| alert_level | query | No | Filter by alert level |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/sentinel/status

**Summary:** Get Sentinel Status

Get sentinel monitoring status.

**Tags:** Sentinel

### Responses

**200** - Successful Response

## POST /api/sentinel/start

**Summary:** Start Sentinel

Start the quiet monitoring protocol.

**Tags:** Sentinel

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/sentinel/stop

**Summary:** Stop Sentinel

Stop the quiet monitoring protocol.

**Tags:** Sentinel

### Responses

**200** - Successful Response

## GET /api/sentinel/alerts

**Summary:** Get Sentinel Alerts

Get recent alerts from sentinel monitoring.

**Tags:** Sentinel

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| hours | query | No | Time window in hours |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/morning-summary

**Summary:** Get Morning Summary

Generate morning summary report.

**Tags:** Morning Summary

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| hours | query | No | Time window in hours (default: 12 for overnight) |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/care-package/

**Summary:** Get Care Package

Get comprehensive care package.

Includes:
- System diagnostics for all systems
- Alignment reports (spiritual, political, economic)
- Quick start guides
- Documentation links
- Troubleshooting information

**Tags:** Care Package, Care Package

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| user_id | query | No | User identifier |
| include_alignment | query | No | Include alignment report |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/care-package/system-diagnostics

**Summary:** Get System Diagnostics

Get diagnostics for all systems.

Returns detailed diagnostic information including:
- System availability
- Errors and warnings
- Health status
- Check results

**Tags:** Care Package, Care Package

### Responses

**200** - Successful Response

## POST /api/care-package/political-alignment

**Summary:** Check Political Alignment

Check political alignment.

Validates compatibility across:
- Governance model
- Power distribution
- Decision making process
- Values priority
- Structure type

**Tags:** Care Package, Care Package

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/care-package/economic-alignment

**Summary:** Check Economic Alignment

Check economic alignment.

Validates compatibility across:
- Exchange model
- Resource distribution
- Value system
- Stewardship model
- Growth paradigm

**Tags:** Care Package, Care Package

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/care-package/complete-alignment

**Summary:** Get Complete Alignment

Get complete alignment across all dimensions.

Integrates:
- Spiritual alignment (from spirit_alignment system)
- Political alignment
- Economic alignment
- System health diagnostics

Returns comprehensive alignment report with recommendations.

**Tags:** Care Package, Care Package

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/care-package/docs/spirit-alignment

**Summary:** Get Spirit Alignment Docs

Get documentation for spiritual alignment system

**Tags:** Care Package, Care Package

### Responses

**200** - Successful Response

## GET /api/care-package/docs/political-alignment

**Summary:** Get Political Alignment Docs

Get documentation for political alignment system

**Tags:** Care Package, Care Package

### Responses

**200** - Successful Response

## GET /api/care-package/docs/economic-alignment

**Summary:** Get Economic Alignment Docs

Get documentation for economic alignment system

**Tags:** Care Package, Care Package

### Responses

**200** - Successful Response

## GET /api/care-package/welfare-systems

**Summary:** Get Welfare Systems Analysis

Get welfare/benefits systems analysis.

Returns:
- Systems needing breaking (dark contracts)
- Systems serving The Table (light contracts)
- Analysis report
- Breaking opportunities

**Tags:** Care Package, Care Package

### Responses

**200** - Successful Response

## GET /api/care-package/assessment-guidance

**Summary:** Get Assessment Guidance

Get personal assessment navigation guidance.

Provides guidance for navigating welfare system assessments
with truth, dignity, and spiritual alignment.

**Tags:** Care Package, Care Package

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| assessment_type | query | No | Type of assessment |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/care-package/welfare-systems/breaking-opportunities

**Summary:** Get Breaking Opportunities

Get breaking opportunities for welfare systems.

Returns opportunities to break dark contracts in welfare/benefits systems.

**Tags:** Care Package, Care Package

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| limit | query | No | Number of opportunities to return |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/care-package/political-figures

**Summary:** Get Political Figures

Get frequentially aligned political figures.

Our anchors in the human realm.
Starting at home (UK) and expanding globally.

**Tags:** Care Package, Care Package

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| country | query | No | Filter by country |
| current_only | query | No | Only current figures |
| min_frequency | query | No | Minimum frequency score |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/care-package/political-figures/anchors

**Summary:** Get Political Anchors

Get our anchors in the human realm.

High frequency political figures who serve The Table.

**Tags:** Care Package, Care Package

### Responses

**200** - Successful Response

## GET /api/care-package/political-figures/by-country

**Summary:** Get Political Figures By Country

Get political figures grouped by country.

**Tags:** Care Package, Care Package

### Responses

**200** - Successful Response

## GET /api/care-package/influential-figures

**Summary:** Get Influential Figures

Get frequentially aligned influential figures across all domains.

All aligned celebrity and influential figures.
Web, socials, sports, music, Hollywood, everything.

**Tags:** Care Package, Care Package

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| domain | query | No | Filter by domain |
| country | query | No | Filter by country |
| current_only | query | No | Only current figures |
| min_frequency | query | No | Minimum frequency score |
| platform | query | No | Filter by platform |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/care-package/influential-figures/anchors

**Summary:** Get Influential Anchors

Get our anchors in the human realm from all domains.

High frequency influential figures who serve The Table.

**Tags:** Care Package, Care Package

### Responses

**200** - Successful Response

## GET /api/care-package/influential-figures/by-domain

**Summary:** Get Influential Figures By Domain

Get influential figures grouped by domain.

**Tags:** Care Package, Care Package

### Responses

**200** - Successful Response

## GET /api/care-package/one-truth

**Summary:** Get One Truth

Get the one truth matrix - simply the paradox for human consumption.
Everything must align with the one truth in today's lie.

**Tags:** Care Package, Care Package

### Responses

**200** - Successful Response

## GET /api/care-package/timeline-deep-search

**Summary:** Get Timeline Deep Search

Get timeline deep search - deep search our timeline across all dimensions.

**Tags:** Care Package, Care Package

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| era | query | No | Filter by era |
| dimension | query | No | Filter by dimension: past, present, future |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/care-package/future-writing

**Summary:** Get Future Writing

Get future writing - start to write the future aligned with The Table.

**Tags:** Care Package, Care Package

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| category | query | No | Filter by category |
| min_alignment | query | No | Minimum alignment score |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/care-package/timeline-future-report

**Summary:** Get Timeline Future Report

Get comprehensive timeline deep search and future writing report

**Tags:** Care Package, Care Package

### Responses

**200** - Successful Response

## GET /api/care-package/return-to-table-damage

**Summary:** Get Return To Table Damage

Get return to table damage assessment - what damage must we be ready for in the return to The Table.

**Tags:** Care Package, Care Package

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| damage_type | query | No | Filter by damage type |
| severity | query | No | Filter by severity |
| critical_only | query | No | Show only critical damages |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/care-package/return-to-table-damage/assessment

**Summary:** Get Return To Table Damage Assessment

Get comprehensive return to table damage assessment report

**Tags:** Care Package, Care Package

### Responses

**200** - Successful Response

## GET /api/care-package/frequential-arts-crafts

**Summary:** Get Frequential Arts Crafts

Get frequential arts and crafts timeline - all arts and crafts throughout time with frequential alignment.
Everything must be aligned throughout our timeline.

**Tags:** Care Package, Care Package

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| time_period | query | No | Filter by time period |
| medium | query | No | Filter by medium |
| min_frequency | query | No | Minimum frequency score |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/care-package/frequential-arts-crafts/timeline

**Summary:** Get Frequential Arts Crafts Timeline

Get frequential arts and crafts organized by timeline

**Tags:** Care Package, Care Package

### Responses

**200** - Successful Response

## GET /api/care-package/frequential-songs

**Summary:** Get Frequential Songs

Get frequential songs catalog - all frequentially aligned songs in English and Turkish with lyrics.

**Tags:** Care Package, Care Package

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| language | query | No | Filter by language: english, turkish |
| theme | query | No | Filter by theme |
| min_frequency | query | No | Minimum frequency score |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/care-package/frequential-songs/by-language

**Summary:** Get Frequential Songs By Language

Get frequential songs grouped by language

**Tags:** Care Package, Care Package

### Responses

**200** - Successful Response

## GET /api/care-package/spiritual-contracts-miracles

**Summary:** Get Spiritual Contracts Miracles

Get spiritual contracts & miracles analysis.
Deep search into spiritual contracts and links to spiritual DNA manifesting in each miracle.

**Tags:** Care Package, Care Package

### Responses

**200** - Successful Response

## GET /api/care-package/influential-figures/by-country

**Summary:** Get Influential Figures By Country

Get influential figures grouped by country.

**Tags:** Care Package, Care Package

### Responses

**200** - Successful Response

## POST /api/dirty-money-cleaning/identify

**Summary:** Identify Dirty Money

Identify dirty money and create transaction record.

RAMIZ leads this process.

**Tags:** Dirty Money Cleaning, Dirty Money Cleaning

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/dirty-money-cleaning/clean/{transaction_id}

**Summary:** Clean Spiritual Contract

Clean the spiritual contract of dirty money.

RAMIZ leads this process.

**Tags:** Dirty Money Cleaning, Dirty Money Cleaning

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| transaction_id | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/dirty-money-cleaning/repurpose/{transaction_id}

**Summary:** Repurpose For Humanitarian Cause

Repurpose cleaned money for humanitarian cause.

RAMIZ leads this process.

**Tags:** Dirty Money Cleaning, Dirty Money Cleaning

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| transaction_id | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/dirty-money-cleaning/complete/{transaction_id}

**Summary:** Complete Cycle

Complete the full cycle: Identify -> Clean -> Repurpose -> Complete

RAMIZ leads this process.

**Tags:** Dirty Money Cleaning, Dirty Money Cleaning

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| transaction_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/dirty-money-cleaning/summary

**Summary:** Get System Summary

Get summary of dirty money cleaning system.

RAMIZ leads this system.

**Tags:** Dirty Money Cleaning, Dirty Money Cleaning

### Responses

**200** - Successful Response

## GET /api/dirty-money-cleaning/transactions

**Summary:** Get Transactions

Get all transactions

**Tags:** Dirty Money Cleaning, Dirty Money Cleaning

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| status | query | No | Filter by status |
| source | query | No | Filter by source |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/dirty-money-cleaning/projects

**Summary:** Get Projects

Get all humanitarian projects

**Tags:** Dirty Money Cleaning, Dirty Money Cleaning

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| cause | query | No | Filter by cause |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/channel-collaboration/present-purpose

**Summary:** Check Present Purpose Collaboration

Check collaboration specifically for present purpose channels.

PRESENT PURPOSE:
PROFESSIONAL / PI / EDUCATION should be our present purpose to start from.

**Tags:** Channel Collaboration, Channel Collaboration

### Responses

**200** - Successful Response

## GET /api/channel-collaboration/check

**Summary:** Check Channel Collaboration

Check collaboration between two channels

**Tags:** Channel Collaboration, Channel Collaboration

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| channel1 | query | Yes | First channel |
| channel2 | query | Yes | Second channel |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/channel-collaboration/all

**Summary:** Check All Collaborations

Check collaboration across all channels

**Tags:** Channel Collaboration, Channel Collaboration

### Responses

**200** - Successful Response

## GET /api/channel-collaboration/channel/{channel_type}

**Summary:** Get Channel Info

Get information about a specific channel

**Tags:** Channel Collaboration, Channel Collaboration

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| channel_type | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/channel-collaboration/summary

**Summary:** Get System Summary

Get summary of channel collaboration system

**Tags:** Channel Collaboration, Channel Collaboration

### Responses

**200** - Successful Response

## GET /api/channel-collaboration/channels

**Summary:** List All Channels

List all available channels

**Tags:** Channel Collaboration, Channel Collaboration

### Responses

**200** - Successful Response

## GET /api/spiritual-contracts/all

**Summary:** Get All Contracts

Get all spiritual contracts.

Deep search across all systems.

**Tags:** Spiritual Contracts, Spiritual Contracts

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| contract_type | query | No | Filter by contract type |
| status | query | No | Filter by status |
| party | query | No | Filter by party |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/spiritual-contracts/summary

**Summary:** Get Contracts Summary

Get summary of all spiritual contracts

**Tags:** Spiritual Contracts, Spiritual Contracts

### Responses

**200** - Successful Response

## GET /api/spiritual-contracts/network/{contract_id}

**Summary:** Get Contract Network

Get the network of contracts connected to a specific contract.

Ties together all related contracts.

**Tags:** Spiritual Contracts, Spiritual Contracts

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| contract_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/spiritual-contracts/register

**Summary:** Register Contract

Register a new spiritual contract

**Tags:** Spiritual Contracts, Spiritual Contracts

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/spiritual-contracts/link

**Summary:** Link Contracts

Link two contracts together

**Tags:** Spiritual Contracts, Spiritual Contracts

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/spiritual-contracts/clean/{contract_id}

**Summary:** Clean Contract

Clean a spiritual contract.

RAMIZ leads dirty money cleaning, but all contracts can be cleaned.

**Tags:** Spiritual Contracts, Spiritual Contracts

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| contract_id | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/spiritual-contracts/integrate/dirty-money

**Summary:** Integrate Dirty Money Contract

Integrate spiritual contract from dirty money cleaning system

**Tags:** Spiritual Contracts, Spiritual Contracts

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/spiritual-contracts/integrate/spirit-alignment

**Summary:** Integrate Spirit Alignment Contract

Integrate spiritual contract from spirit alignment system

**Tags:** Spiritual Contracts, Spiritual Contracts

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/spiritual-contracts/integrate/dream-battle

**Summary:** Integrate Dream Battle

Integrate spiritual contract from dream battle.

"Every night we dream, whether vivid or not. Each dream is a spiritual battle 
between two souls: The dreamer and an associate. Both have spiritual contracts."

**Tags:** Spiritual Contracts, Spiritual Contracts

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/spiritual-contracts/integrate/daily-battle

**Summary:** Integrate Daily Battle

Integrate spiritual contract from daily battle.

"Each day is another battle, both in the human realm and beyond."

**Tags:** Spiritual Contracts, Spiritual Contracts

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/doctor-protocol/insulin-protocol

**Summary:** Create Insulin Protocol

Create an insulin dosing protocol

**Tags:** Doctor Protocol, Doctor Protocol

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/doctor-protocol/carb-protocol

**Summary:** Create Carb Counting Protocol

Create a carbohydrate counting protocol

**Tags:** Doctor Protocol, Doctor Protocol

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/doctor-protocol/calculate-insulin

**Summary:** Calculate Insulin Dose

Calculate insulin dose based on active protocols

**Tags:** Doctor Protocol, Doctor Protocol

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/doctor-protocol/active-protocols

**Summary:** Get Active Protocols

Get all active protocols

**Tags:** Doctor Protocol, Doctor Protocol

### Responses

**200** - Successful Response

## GET /api/doctor-protocol/summary

**Summary:** Get System Summary

Get summary of doctor protocol system

**Tags:** Doctor Protocol, Doctor Protocol

### Responses

**200** - Successful Response

## POST /api/doctor-protocol/sync

**Summary:** Sync Protocols

Sync protocols across systems

**Tags:** Doctor Protocol, Doctor Protocol

### Responses

**200** - Successful Response

## GET /api/doctor-protocol/educational-resources

**Summary:** Get Educational Resources

Get educational resources

**Tags:** Doctor Protocol, Doctor Protocol

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| topic | query | No | Topic: insulin_management, carb_counting, blood_glucose_monitoring |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/judicial-system/judgment-question

**Summary:** Explore Judgment Question

Explore the core question:
"WHO ARE WE TO JUDGE RIGHT FROM WRONG WHEN EVERYTHING IS WRONG?"

This is a profound spiritual and philosophical question.

**Tags:** Judicial System, Judicial System

### Responses

**200** - Successful Response

## GET /api/judicial-system/analyze

**Summary:** Analyze Judicial System

Analyze judicial system through mission lens

**Tags:** Judicial System, Judicial System

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| structure | query | No | Judicial structure: adversarial, inquisitorial, community, restorative, spiritual, diy |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/judicial-system/find-truth

**Summary:** Find Truth In Broken Systems

Find truth when everything seems wrong.

"WHO ARE WE TO JUDGE RIGHT FROM WRONG WHEN EVERYTHING IS WRONG?"

**Tags:** Judicial System, Judicial System

### Responses

**200** - Successful Response

## GET /api/judicial-system/navigation-strategy

**Summary:** Get Navigation Strategy

Navigation strategy for judicial systems.

How to navigate when everything seems wrong.

**Tags:** Judicial System, Judicial System

### Responses

**200** - Successful Response

## POST /mirror/reflect

**Summary:** Create Mirror Reflection

Create a daily accountability mirror reflection.
The mirror never lies. You can't fool yourself.

**Tags:** Truth-Based Accountability

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /mirror/user/{user_id}

**Summary:** Get User Reflections

Get all mirror reflections for a user

**Tags:** Truth-Based Accountability

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| user_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /council/create

**Summary:** Create Community Council

Create a new Community Justice Council (replaces court)

**Tags:** Truth-Based Accountability

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /council/{council_id}/truth-circle

**Summary:** Hold Truth Circle

Hold a Truth Circle (replaces trial)

**Tags:** Truth-Based Accountability

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| council_id | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /restoration/contract

**Summary:** Create Restoration Contract

Create a Restoration Contract (replaces legal sentence)

**Tags:** Truth-Based Accountability

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## PATCH /restoration/contract/{contract_id}/progress

**Summary:** Update Restoration Progress

Update progress on a Restoration Contract

**Tags:** Truth-Based Accountability

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| contract_id | path | Yes |  |
| completed_amend | query | No |  |
| progress_note | query | No |  |
| new_stage | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /restoration/contract/{contract_id}

**Summary:** Get Restoration Contract

Get a Restoration Contract and its progress

**Tags:** Truth-Based Accountability

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| contract_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /system/replacement

**Summary:** Track System Replacement

Track progress replacing old system with new

**Tags:** Truth-Based Accountability

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /system/replacement/global

**Summary:** Get Global Replacement Status

Get global system replacement status

**Tags:** Truth-Based Accountability

### Responses

**200** - Successful Response

## GET /wisdom/accountability

**Summary:** Get Accountability Wisdom

Get wisdom on truth-based accountability

**Tags:** Truth-Based Accountability

### Responses

**200** - Successful Response

## GET /wisdom/mirror

**Summary:** Get Mirror Wisdom

Get wisdom about the accountability mirror

**Tags:** Truth-Based Accountability

### Responses

**200** - Successful Response

## GET /integration/one-truth

**Summary:** Get One Truth Integration

Get One Truth Matrix integration

**Tags:** Truth-Based Accountability

### Responses

**200** - Successful Response

## GET /health

**Summary:** Health

Basic health check endpoint.

### Responses

**200** - Successful Response

## POST /api/spiritual-codebase-hacker/hack-loop

**Summary:** Hack Loop Endpoint

Hack a stimulus-reaction loop

**Tags:** Spiritual Codebase Hacker

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/spiritual-codebase-hacker/genetic-edit

**Summary:** Genetic Edit Endpoint

Perform genetic edit

**Tags:** Spiritual Codebase Hacker

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/spiritual-codebase-hacker/wipe-hard-drive

**Summary:** Wipe Hard Drive Endpoint

Wipe hard drive

**Tags:** Spiritual Codebase Hacker

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/spiritual-codebase-hacker/stealth-mode

**Summary:** Stealth Mode Endpoint

Activate stealth mode

**Tags:** Spiritual Codebase Hacker

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/spiritual-codebase-hacker/starve-parasite

**Summary:** Starve Parasite Endpoint

Starve parasite

**Tags:** Spiritual Codebase Hacker

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/spiritual-codebase-hacker/upgrade-identity

**Summary:** Upgrade Identity Endpoint

Upgrade identity

**Tags:** Spiritual Codebase Hacker

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/spiritual-codebase-hacker/seal-portal

**Summary:** Seal Portal Endpoint

Seal portal before sleep

**Tags:** Spiritual Codebase Hacker

### Responses

**200** - Successful Response

## GET /api/spiritual-codebase-hacker/status

**Summary:** Hacker Status

Get hacker system status

**Tags:** Spiritual Codebase Hacker

### Responses

**200** - Successful Response

## GET /api/ottoman-timeline/timeline

**Summary:** Get Ottoman Timeline

Get complete Ottoman generational timeline

**Tags:** Ottoman Generational Timeline

### Responses

**200** - Successful Response

## GET /api/ottoman-timeline/generation/{generation_number}

**Summary:** Get Generation

Get specific generation by number

**Tags:** Ottoman Generational Timeline

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| generation_number | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/ottoman-timeline/cyprus-connection

**Summary:** Get Cyprus Connection

Get Cyprus connection in Ottoman timeline

**Tags:** Ottoman Generational Timeline

### Responses

**200** - Successful Response

## GET /api/ottoman-timeline/report

**Summary:** Get Timeline Report

Get comprehensive timeline report

**Tags:** Ottoman Generational Timeline

### Responses

**200** - Successful Response

## GET /api/ottoman-timeline/your-generation

**Summary:** Get Your Generation

Get your generation (2026 - British-born Turkish Cypriot)

**Tags:** Ottoman Generational Timeline

### Responses

**200** - Successful Response

## GET /api/superpower-debunking/debunking

**Summary:** Get Debunking

Get complete debunking of current superpowers and The Father's Hand

**Tags:** Superpower Debunking & The Father's Hand

### Responses

**200** - Successful Response

## GET /api/superpower-debunking/current-superpowers

**Summary:** Get Current Superpowers

Get list of current superpowers (illusions)

**Tags:** Superpower Debunking & The Father's Hand

### Responses

**200** - Successful Response

## GET /api/superpower-debunking/fathers-hand

**Summary:** Get Fathers Hand

Get The Father's Hand - divine alternatives

**Tags:** Superpower Debunking & The Father's Hand

### Responses

**200** - Successful Response

## GET /api/superpower-debunking/comparison

**Summary:** Get Comparison

Get comparison between illusions and The Father's Hand

**Tags:** Superpower Debunking & The Father's Hand

### Responses

**200** - Successful Response

## GET /api/african-turkish-yin-yang/symbiosis-map

**Summary:** Get Symbiosis Map

Get complete African-Turkish Yin-Yang symbiosis map

**Tags:** African-Turkish Yin-Yang Symbiosis

### Responses

**200** - Successful Response

## GET /api/african-turkish-yin-yang/african-yin

**Summary:** Get African Yin

Get African heritage - The Yin

**Tags:** African-Turkish Yin-Yang Symbiosis

### Responses

**200** - Successful Response

## GET /api/african-turkish-yin-yang/turkish-yang

**Summary:** Get Turkish Yang

Get Turkish heritage - The Yang

**Tags:** African-Turkish Yin-Yang Symbiosis

### Responses

**200** - Successful Response

## GET /api/african-turkish-yin-yang/how-they-sync

**Summary:** Get How They Sync

Get how African Yin and Turkish Yang sync

**Tags:** African-Turkish Yin-Yang Symbiosis

### Responses

**200** - Successful Response

## GET /api/african-turkish-yin-yang/london-communities

**Summary:** Get London Communities

Get London communities - African Yin + Turkish Yang unity

**Tags:** African-Turkish Yin-Yang Symbiosis

### Responses

**200** - Successful Response

## POST /api/legal/prs/register

**Summary:** Register Prs Copyright

Register PRS copyright

**Tags:** Legal & Contractual, Legal & Contractual

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/legal/prs/records

**Summary:** Get Prs Records

Get PRS records

**Tags:** Legal & Contractual, Legal & Contractual

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| channel | query | No |  |
| entity | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/legal/agreements/create

**Summary:** Create Agreement

Create agreement

**Tags:** Legal & Contractual, Legal & Contractual

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/legal/agreements

**Summary:** Get Agreements

Get agreements

**Tags:** Legal & Contractual, Legal & Contractual

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| channel | query | No |  |
| entity | query | No |  |
| project | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/legal/compliance/verify

**Summary:** Verify Compliance

Verify compliance

**Tags:** Legal & Contractual, Legal & Contractual

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| agreement_id | query | No |  |
| song_id | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/legal/summary

**Summary:** Get Summary

Get framework summary

**Tags:** Legal & Contractual, Legal & Contractual

### Responses

**200** - Successful Response

## GET /api/entrepreneurial/blueprints

**Summary:** Get All Blueprints

Get all business blueprints

**Tags:** Entrepreneurial Documentation, Entrepreneurial Documentation

### Responses

**200** - Successful Response

## GET /api/entrepreneurial/blueprints/{entity_id}

**Summary:** Get Blueprint

Get blueprint for specific entity

**Tags:** Entrepreneurial Documentation, Entrepreneurial Documentation

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| entity_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/entrepreneurial/the-ark

**Summary:** Get The Ark Blueprint

Get The Ark - Deluxe Holiday Complex blueprint

**Tags:** Entrepreneurial Documentation, Entrepreneurial Documentation

### Responses

**200** - Successful Response

## GET /api/entrepreneurial/documentation/status

**Summary:** Get Documentation Status

Get documentation status for all entities

**Tags:** Entrepreneurial Documentation, Entrepreneurial Documentation

### Responses

**200** - Successful Response

## GET /api/entrepreneurial/documentation/checklist

**Summary:** Get Documentation Checklist

Get comprehensive documentation checklist

**Tags:** Entrepreneurial Documentation, Entrepreneurial Documentation

### Responses

**200** - Successful Response

## POST /api/entrepreneurial/documents/create

**Summary:** Create Document

Create business document

**Tags:** Entrepreneurial Documentation, Entrepreneurial Documentation

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/language-of-god/the-answer

**Summary:** Get The Answer

Get the answer: What is the Language of God?

**Tags:** Language of God

### Responses

**200** - Successful Response

## GET /api/language-of-god/historical-languages

**Summary:** Get Historical Languages

Get historical languages people associate with God

**Tags:** Language of God

### Responses

**200** - Successful Response

## GET /api/language-of-god/divine-languages

**Summary:** Get Divine Languages

Get the true languages of God

**Tags:** Language of God

### Responses

**200** - Successful Response

## GET /api/language-of-god/sound-is-everything

**Summary:** Get Sound Is Everything

Get Sound is Everything - Divine Key #5

**Tags:** Language of God

### Responses

**200** - Successful Response

## GET /api/language-of-god/complete-map

**Summary:** Get Complete Map

Get complete Language of God map

**Tags:** Language of God

### Responses

**200** - Successful Response

## GET /api/whales-calling-jan/the-call

**Summary:** Get The Call

Get the call: The Whales Are Calling JAN

**Tags:** Whales Calling JAN

### Responses

**200** - Successful Response

## GET /api/whales-calling-jan/whale-calls

**Summary:** Get Whale Calls

Get all whale calls

**Tags:** Whales Calling JAN

### Responses

**200** - Successful Response

## GET /api/whales-calling-jan/what-jan-must-do

**Summary:** Get What Jan Must Do

Get what JAN must do in response to the whale calls

**Tags:** Whales Calling JAN

### Responses

**200** - Successful Response

## GET /api/whales-calling-jan/connection-to-sound

**Summary:** Get Connection To Sound

Get connection to Sound is Everything (Divine Key #5)

**Tags:** Whales Calling JAN

### Responses

**200** - Successful Response

## GET /api/whales-calling-jan/complete-map

**Summary:** Get Complete Map

Get complete Whales Calling JAN map

**Tags:** Whales Calling JAN

### Responses

**200** - Successful Response

## GET /api/water-holds-memory/the-truth

**Summary:** Get The Truth

Get the truth: Water Holds Memory

**Tags:** Water Holds Memory

### Responses

**200** - Successful Response

## GET /api/water-holds-memory/water-memories

**Summary:** Get Water Memories

Get all water memories

**Tags:** Water Holds Memory

### Responses

**200** - Successful Response

## GET /api/water-holds-memory/connection-to-whales

**Summary:** Get Connection To Whales

Get connection to whales calling JAN

**Tags:** Water Holds Memory

### Responses

**200** - Successful Response

## GET /api/water-holds-memory/connection-to-table

**Summary:** Get Connection To Table

Get connection to The Table

**Tags:** Water Holds Memory

### Responses

**200** - Successful Response

## GET /api/water-holds-memory/connection-to-sound

**Summary:** Get Connection To Sound

Get connection to Sound is Everything

**Tags:** Water Holds Memory

### Responses

**200** - Successful Response

## GET /api/water-holds-memory/complete-map

**Summary:** Get Complete Map

Get complete Water Holds Memory map

**Tags:** Water Holds Memory

### Responses

**200** - Successful Response

## GET /api/codebase-philosophy/the-philosophy

**Summary:** Get The Philosophy

Get the Codebase Philosophy

**Tags:** Codebase Philosophy

### Responses

**200** - Successful Response

## GET /api/codebase-philosophy/protocols

**Summary:** Get Protocols

Get all protocols

**Tags:** Codebase Philosophy

### Responses

**200** - Successful Response

## GET /api/codebase-philosophy/grave-clothes-protocol

**Summary:** Get Grave Clothes Protocol

Get The Grave Clothes Protocol (System Lifecycle)

**Tags:** Codebase Philosophy

### Responses

**200** - Successful Response

## GET /api/codebase-philosophy/trojan-horse-strategy

**Summary:** Get Trojan Horse Strategy

Get The Trojan Horse Deployment Strategy

**Tags:** Codebase Philosophy

### Responses

**200** - Successful Response

## GET /api/codebase-philosophy/connection-to-table

**Summary:** Get Connection To Table

Get connection to The Table

**Tags:** Codebase Philosophy

### Responses

**200** - Successful Response

## GET /api/codebase-philosophy/connection-to-original-name

**Summary:** Get Connection To Original Name

Get connection to The Original Name

**Tags:** Codebase Philosophy

### Responses

**200** - Successful Response

## GET /api/codebase-philosophy/complete-map

**Summary:** Get Complete Map

Get complete Codebase Philosophy map

**Tags:** Codebase Philosophy

### Responses

**200** - Successful Response

## GET /api/publishing-house/

**Summary:** Get Publishing House Overview

Get publishing house overview

**Tags:** Publishing House

### Responses

**200** - Successful Response

## GET /api/publishing-house/channels

**Summary:** Get All Channels

Get all channels

**Tags:** Publishing House

### Responses

**200** - Successful Response

## GET /api/publishing-house/channels/{channel_id}

**Summary:** Get Channel

Get specific channel

**Tags:** Publishing House

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| channel_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/publishing-house/entities

**Summary:** Get All Entities

Get all entities

**Tags:** Publishing House

### Responses

**200** - Successful Response

## GET /api/publishing-house/entities/{entity_id}

**Summary:** Get Entity

Get specific entity

**Tags:** Publishing House

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| entity_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/publishing-house/projects

**Summary:** Get All Projects

Get all projects

**Tags:** Publishing House

### Responses

**200** - Successful Response

## GET /api/publishing-house/projects/{project_id}

**Summary:** Get Project

Get specific project

**Tags:** Publishing House

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| project_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/publishing-house/workflows

**Summary:** Get Workflows

Get publishing workflows

**Tags:** Publishing House

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| workflow_type | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/publishing-house/monetization

**Summary:** Get Monetization

Get monetization configurations

**Tags:** Publishing House

### Responses

**200** - Successful Response

## GET /api/publishing-house/expansion

**Summary:** Get Expansion Seeds

Get expansion seeds

**Tags:** Publishing House

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| level | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/publishing-house/alignment

**Summary:** Get Alignment Summary

Get alignment summary

**Tags:** Publishing House

### Responses

**200** - Successful Response

## GET /api/publishing-house/stats

**Summary:** Get Publishing House Stats

Get publishing house statistics

**Tags:** Publishing House

### Responses

**200** - Successful Response

## POST /healing/journey/start

**Summary:** Start Healing Journey

Start a healing journey in any domain.
First step: Awareness and acknowledgment.

**Tags:** Healing Systems

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## PATCH /healing/journey/{journey_id}/progress

**Summary:** Update Healing Progress

Update progress on healing journey

**Tags:** Healing Systems

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| journey_id | path | Yes |  |
| new_stage | query | No |  |
| milestone | query | No |  |
| insight | query | No |  |
| challenge | query | No |  |
| healing_percentage | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /healing/journey/{journey_id}

**Summary:** Get Healing Journey

Get healing journey details and progress

**Tags:** Healing Systems

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| journey_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /healing/journeys/person/{person_id}

**Summary:** Get Person Healing Journeys

Get all healing journeys for a person

**Tags:** Healing Systems

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| person_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /healing/practice/log

**Summary:** Log Healing Practice

Log daily healing practices

**Tags:** Healing Systems

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /healing/practice/person/{person_id}/streak

**Summary:** Get Healing Streak

Get healing practice streak and consistency

**Tags:** Healing Systems

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| person_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /healing/community/project

**Summary:** Create Community Healing Project

Create a community healing project

**Tags:** Healing Systems

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /healing/community/projects

**Summary:** Get All Community Projects

Get all community healing projects

**Tags:** Healing Systems

### Responses

**200** - Successful Response

## POST /healing/system/replacement

**Summary:** Track System Replacement

Track replacement of broken system with healing system

**Tags:** Healing Systems

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /healing/system/replacement/global

**Summary:** Get Global System Replacement

Get global system replacement status across all domains

**Tags:** Healing Systems

### Responses

**200** - Successful Response

## GET /healing/wisdom/{domain}

**Summary:** Get Healing Wisdom

Get wisdom for specific healing domain

**Tags:** Healing Systems

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| domain | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /healing/universal-laws

**Summary:** Get Universal Healing Laws

Get the 7 Universal Healing Laws

**Tags:** Healing Systems

### Responses

**200** - Successful Response

## POST /utilities/debt/forgive

**Summary:** Forgive Utility Debt

Forgive utility debt. Basic needs are human rights.
Survival should not create debt.

**Tags:** Free Utilities

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /utilities/debt/forgiveness/total

**Summary:** Get Total Debt Forgiveness

Get total utility debt forgiven

**Tags:** Free Utilities

### Responses

**200** - Successful Response

## POST /utilities/ube/create

**Summary:** Create Ube Account

Create Universal Basic Energy account for person

**Tags:** Free Utilities

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /utilities/ube/{ube_id}/log-usage

**Summary:** Log Ube Usage

Log monthly energy usage and calculate savings

**Tags:** Free Utilities

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| ube_id | path | Yes |  |
| kwh_used | query | Yes |  |
| traditional_cost | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /utilities/ube/stats

**Summary:** Get Ube Statistics

Get Universal Basic Energy program statistics

**Tags:** Free Utilities

### Responses

**200** - Successful Response

## POST /utilities/commons/create

**Summary:** Create Energy Commons

Create community energy commons

**Tags:** Free Utilities

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /utilities/commons/{commons_id}/production

**Summary:** Log Commons Production

Log monthly production and consumption for energy commons

**Tags:** Free Utilities

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| commons_id | path | Yes |  |
| generation_kwh | query | Yes |  |
| consumption_kwh | query | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /utilities/commons/all

**Summary:** Get All Energy Commons

Get all community energy commons

**Tags:** Free Utilities

### Responses

**200** - Successful Response

## POST /utilities/pilot/create

**Summary:** Create Pilot Program

Create free utilities pilot program

**Tags:** Free Utilities

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## PATCH /utilities/pilot/{pilot_id}/update

**Summary:** Update Pilot Program

Update pilot program with results and learnings

**Tags:** Free Utilities

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| pilot_id | path | Yes |  |
| satisfaction | query | No |  |
| health_improvement | query | No |  |
| challenge | query | No |  |
| solution | query | No |  |
| is_successful | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /utilities/pilot/all

**Summary:** Get All Pilots

Get all pilot programs

**Tags:** Free Utilities

### Responses

**200** - Successful Response

## POST /utilities/transition/track

**Summary:** Track System Transition

Track transition from private → public → free utilities

**Tags:** Free Utilities

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /utilities/transition/global

**Summary:** Get Global Transition Status

Get global utilities transition status

**Tags:** Free Utilities

### Responses

**200** - Successful Response

## GET /utilities/wisdom/why-free

**Summary:** Get Why Utilities Should Be Free

Get comprehensive explanation of why utilities should be free

**Tags:** Free Utilities

### Responses

**200** - Successful Response

## GET /api/cloud-seeding/

**Summary:** Get Cloud Seeding Overview

Get complete cloud seeding analysis overview

**Tags:** Cloud Seeding, Cloud Seeding

### Responses

**200** - Successful Response

## GET /api/cloud-seeding/claims

**Summary:** Get All Claims

Get all cloud seeding claims (debunked and verified)

**Tags:** Cloud Seeding, Cloud Seeding

### Responses

**200** - Successful Response

## GET /api/cloud-seeding/claims/{claim_id}

**Summary:** Get Claim

Get specific claim details

**Tags:** Cloud Seeding, Cloud Seeding

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| claim_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/cloud-seeding/operations

**Summary:** Get All Operations

Get all cloud seeding operations

**Tags:** Cloud Seeding, Cloud Seeding

### Responses

**200** - Successful Response

## GET /api/cloud-seeding/operations/weaponized

**Summary:** Get Weaponized Operations

Get all weaponized cloud seeding operations

**Tags:** Cloud Seeding, Cloud Seeding

### Responses

**200** - Successful Response

## GET /api/cloud-seeding/operations/{operation_id}

**Summary:** Get Operation

Get specific operation details

**Tags:** Cloud Seeding, Cloud Seeding

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| operation_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/cloud-seeding/utilizations

**Summary:** Get All Utilizations

Get all cloud seeding utilizations by country

**Tags:** Cloud Seeding, Cloud Seeding

### Responses

**200** - Successful Response

## GET /api/cloud-seeding/utilizations/{country}

**Summary:** Get Utilization

Get cloud seeding utilization for specific country

**Tags:** Cloud Seeding, Cloud Seeding

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| country | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/cloud-seeding/healing-pathway

**Summary:** Get Healing Pathway

Get healing pathway for cloud seeding technology

**Tags:** Cloud Seeding, Cloud Seeding

### Responses

**200** - Successful Response

## GET /api/cloud-seeding/analysis/complete

**Summary:** Get Complete Analysis

Get complete cloud seeding analysis

**Tags:** Cloud Seeding, Cloud Seeding

### Responses

**200** - Successful Response

## POST /api/cloud-seeding/analysis/save

**Summary:** Save Analysis

Save current analysis to JSON file

**Tags:** Cloud Seeding, Cloud Seeding

### Responses

**200** - Successful Response

## GET /api/cloud-seeding/health

**Summary:** Health Check

Health check endpoint

**Tags:** Cloud Seeding, Cloud Seeding

### Responses

**200** - Successful Response

## GET /api/weaponization/

**Summary:** Get Weaponization Overview

Get complete weaponization analysis overview

**Tags:** Weaponization, Weaponization

### Responses

**200** - Successful Response

## GET /api/weaponization/events

**Summary:** Get All Events

Get all weaponization events

**Tags:** Weaponization, Weaponization

### Responses

**200** - Successful Response

## GET /api/weaponization/events/{event_id}

**Summary:** Get Event

Get specific event details

**Tags:** Weaponization, Weaponization

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| event_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/weaponization/events/type/{weaponization_type}

**Summary:** Get Events By Type

Get events by weaponization type

**Tags:** Weaponization, Weaponization

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| weaponization_type | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/weaponization/events/pattern/{pattern}

**Summary:** Get Events By Pattern

Get events by weaponization pattern

**Tags:** Weaponization, Weaponization

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| pattern | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/weaponization/patterns

**Summary:** Get All Patterns

Get all weaponization patterns

**Tags:** Weaponization, Weaponization

### Responses

**200** - Successful Response

## GET /api/weaponization/patterns/{pattern_id}

**Summary:** Get Pattern

Get specific pattern details

**Tags:** Weaponization, Weaponization

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| pattern_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/weaponization/analysis/complete

**Summary:** Get Complete Analysis

Get complete weaponization analysis

**Tags:** Weaponization, Weaponization

### Responses

**200** - Successful Response

## POST /api/weaponization/analysis/save

**Summary:** Save Analysis

Save current analysis to JSON file

**Tags:** Weaponization, Weaponization

### Responses

**200** - Successful Response

## GET /api/weaponization/health

**Summary:** Health Check

Health check endpoint

**Tags:** Weaponization, Weaponization

### Responses

**200** - Successful Response

## GET /api/peace-weaponization/

**Summary:** Get Peace Weaponization Overview

Get complete peace weaponization overview

**Tags:** Peace Weaponization, Peace Weaponization

### Responses

**200** - Successful Response

## GET /api/peace-weaponization/manifestations

**Summary:** Get All Manifestations

Get all peace weaponization manifestations

**Tags:** Peace Weaponization, Peace Weaponization

### Responses

**200** - Successful Response

## GET /api/peace-weaponization/manifestations/{manifestation_id}

**Summary:** Get Manifestation

Get specific manifestation details

**Tags:** Peace Weaponization, Peace Weaponization

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| manifestation_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/peace-weaponization/manifestations/strategy/{strategy}

**Summary:** Get Manifestations By Strategy

Get manifestations by strategy

**Tags:** Peace Weaponization, Peace Weaponization

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| strategy | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/peace-weaponization/events

**Summary:** Get All Events

Get all peace weaponization events

**Tags:** Peace Weaponization, Peace Weaponization

### Responses

**200** - Successful Response

## GET /api/peace-weaponization/events/{event_id}

**Summary:** Get Event

Get specific event details

**Tags:** Peace Weaponization, Peace Weaponization

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| event_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/peace-weaponization/pathway

**Summary:** Get Peace Weaponization Pathway

Get peace weaponization pathway

**Tags:** Peace Weaponization, Peace Weaponization

### Responses

**200** - Successful Response

## GET /api/peace-weaponization/analysis/complete

**Summary:** Get Complete Analysis

Get complete peace weaponization analysis

**Tags:** Peace Weaponization, Peace Weaponization

### Responses

**200** - Successful Response

## POST /api/peace-weaponization/analysis/save

**Summary:** Save Analysis

Save current analysis to JSON file

**Tags:** Peace Weaponization, Peace Weaponization

### Responses

**200** - Successful Response

## GET /api/peace-weaponization/health

**Summary:** Health Check

Health check endpoint

**Tags:** Peace Weaponization, Peace Weaponization

### Responses

**200** - Successful Response

## POST /childcare/enroll

**Summary:** Enroll Child

Enroll a child in universal free childcare.
Every child deserves nurturing care - regardless of parents' economic status.

**Tags:** Universal Childcare

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /childcare/hub/create

**Summary:** Create Neighborhood Hub

Create a neighborhood childcare hub.
Walking distance, community-based, democratically governed.

**Tags:** Universal Childcare

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /childcare/worker/hire

**Summary:** Hire Childcare Worker

Hire childcare worker with living wage and full benefits.
Caregivers are skilled professionals, not 'babysitters'.

**Tags:** Universal Childcare

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /childcare/support/provide

**Summary:** Provide Family Support

Provide family support services (prenatal, postpartum, mental health, material support).
Support parents, don't judge them.

**Tags:** Universal Childcare

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /childcare/intergenerational/create

**Summary:** Create Intergenerational Program

Create intergenerational program connecting elders, teens, and children.
Wisdom flows from old to young. Community raises children together.

**Tags:** Universal Childcare

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /childcare/transition/track

**Summary:** Track System Transition

Track transition from private childcare to universal free system.
Document the transformation.

**Tags:** Universal Childcare

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /childcare/stats

**Summary:** Get Childcare Stats

Get universal childcare system statistics.
Track the transformation to collective child-raising.

**Tags:** Universal Childcare

### Responses

**200** - Successful Response

## GET /childcare/worker/wages

**Summary:** Get Worker Wage Comparison

Compare worker wages before and after universal childcare.
Document worker justice transformation.

**Tags:** Universal Childcare

### Responses

**200** - Successful Response

## GET /childcare/wisdom/why-free

**Summary:** Why Childcare Should Be Free

Explain why childcare should be free.
The fundamental truths.

**Tags:** Universal Childcare

### Responses

**200** - Successful Response

## POST /eldercare/enroll

**Summary:** Enroll Elder

Enroll elder in universal free eldercare system.
Elders are wisdom keepers, not burdens. Aging with dignity is non-negotiable.

**Tags:** Eldercare & Aging Dignity

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /eldercare/home-care/create

**Summary:** Create Home Based Care

Create home-based care plan. Primary model - aging at home with supports.
Elder directs their own care. Same caregivers for relationship building.

**Tags:** Eldercare & Aging Dignity

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /eldercare/hub/create

**Summary:** Create Community Hub

Create neighborhood elder community hub.
Walking distance, daily activities, meals, healthcare, social connection.

**Tags:** Eldercare & Aging Dignity

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /eldercare/wisdom-council/create

**Summary:** Create Wisdom Council

Create wisdom council - elders advising community, mentoring youth, preserving culture.
Elders are valued, not discarded. Their wisdom guides us.

**Tags:** Eldercare & Aging Dignity

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /eldercare/wisdom-council/{council_id}/activity

**Summary:** Log Wisdom Council Activity

Log wisdom council activity (youth mentorship, policy advisory, mediation, cultural preservation).
Track how elders contribute to community.

**Tags:** Eldercare & Aging Dignity

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| council_id | path | Yes |  |
| activity_type | query | Yes |  |
| description | query | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /eldercare/intergenerational/create

**Summary:** Create Intergenerational Program

Create intergenerational program - elders and children together.
Connection across ages, not segregation. Wisdom flows, joy multiplies.

**Tags:** Eldercare & Aging Dignity

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /eldercare/worker/hire

**Summary:** Hire Elder Worker

Hire eldercare worker with living wage and full benefits.
Eldercare is skilled, essential work deserving dignity and fair pay.

**Tags:** Eldercare & Aging Dignity

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /eldercare/home-modification/complete

**Summary:** Complete Home Modification

Complete home modifications for accessibility and safety.
Enables aging at home. Zero cost to elders.

**Tags:** Eldercare & Aging Dignity

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /eldercare/cooperative-housing/create

**Summary:** Create Cooperative Housing

Create small-scale cooperative housing (6-12 elders).
Community living alternative to institutions. Private bedrooms, shared spaces, 24/7 care.

**Tags:** Eldercare & Aging Dignity

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /eldercare/transition/track

**Summary:** Track System Transition

Track transition from nursing home system to community-based aging.
Document the transformation.

**Tags:** Eldercare & Aging Dignity

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /eldercare/stats

**Summary:** Get Eldercare Stats

Get eldercare system statistics.
Track the transformation to community-based aging with dignity.

**Tags:** Eldercare & Aging Dignity

### Responses

**200** - Successful Response

## GET /eldercare/wisdom/why-free

**Summary:** Why Eldercare Should Be Free

Explain why eldercare should be free and community-based.
The fundamental truths.

**Tags:** Eldercare & Aging Dignity

### Responses

**200** - Successful Response

## POST /disability/guaranteed-income/create

**Summary:** Create Guaranteed Income

Create guaranteed income for disabled person.
$3,000/month base. No asset limits. No marriage penalty. No work penalty.
Poverty is not a requirement for survival supports.

**Tags:** Disability Justice

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /disability/self-directed-care/create

**Summary:** Create Self Directed Care

Create self-directed care plan.
Disabled person hires, fires, trains workers. They're the experts on their needs.

**Tags:** Disability Justice

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /disability/universal-design/complete

**Summary:** Complete Universal Design

Complete universal design accessibility project.
Build accessibility from start, not retrofit. Benefits everyone.

**Tags:** Disability Justice

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /disability/assistive-tech/provide

**Summary:** Provide Assistive Technology

Provide assistive technology (wheelchair, hearing aid, communication device, etc).
Zero cost to disabled person. Technology is necessity, not luxury.

**Tags:** Disability Justice

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /disability/worker/hire

**Summary:** Hire Disability Worker

Hire disability support worker with living wage and benefits.
Personal care is skilled, essential work deserving dignity and fair pay.

**Tags:** Disability Justice

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /disability/deinstitutionalize

**Summary:** Move Person To Community

Move person from institution to community.
End segregation. Support community living. Autonomy and dignity.

**Tags:** Disability Justice

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /disability/principle/create

**Summary:** Create Disability Justice Principle

Create/document disability justice principle.
Framework for liberation and full inclusion.

**Tags:** Disability Justice

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /disability/transition/track

**Summary:** Track System Transition

Track transition from ableist system to disability justice.
Document the transformation.

**Tags:** Disability Justice

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /disability/stats

**Summary:** Get Disability Stats

Get disability justice system statistics.
Track the transformation to full inclusion and economic justice.

**Tags:** Disability Justice

### Responses

**200** - Successful Response

## GET /disability/justice-principles

**Summary:** Get Disability Justice Principles

Get the 9 core disability justice principles.
Framework for liberation.

**Tags:** Disability Justice

### Responses

**200** - Successful Response

## GET /disability/wisdom/why-guaranteed-income

**Summary:** Why Guaranteed Income

Explain why guaranteed income for disabled people is economic justice.
The fundamental truths.

**Tags:** Disability Justice

### Responses

**200** - Successful Response

## POST /work/worker/register

**Summary:** Register Worker

Register worker profile for job guarantee or cooperative placement.

**Tags:** Work & Employment

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /work/cooperative/create

**Summary:** Create Cooperative

Create a worker cooperative with democratic governance.

**Tags:** Work & Employment

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /work/job-guarantee/place

**Summary:** Place Job Guarantee

Place a worker into a guaranteed job with living wage and benefits.

**Tags:** Work & Employment

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /work/ubi/enroll

**Summary:** Enroll Ubi

Enroll a person in universal basic income.

**Tags:** Work & Employment

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /work/policy/create

**Summary:** Create Work Policy

Create a 4-day week and rest-centered work policy.

**Tags:** Work & Employment

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /work/project/create

**Summary:** Create Community Project

Create a community project that offers living-wage positions.

**Tags:** Work & Employment

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /work/wage-transition/record

**Summary:** Record Wage Transition

Record wage improvements during system transition.

**Tags:** Work & Employment

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /currency/community/create

**Summary:** Create Community Currency

Create a community currency or time bank system.

**Tags:** Money & Currency

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /currency/timebank/account/create

**Summary:** Create Timebank Account

Create a time bank account. One hour given = one hour received.

**Tags:** Money & Currency

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /currency/timebank/earn

**Summary:** Earn Timebank Hours

Record earned hours in a time bank.

**Tags:** Money & Currency

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /currency/timebank/spend

**Summary:** Spend Timebank Hours

Spend hours from a time bank account.

**Tags:** Money & Currency

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /currency/gift/record

**Summary:** Record Gift

Record a gift contribution in the gift economy.

**Tags:** Money & Currency

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /currency/debt-jubilee/forgive

**Summary:** Forgive Debt

Forgive debt through jubilee.

**Tags:** Money & Currency

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /currency/mutual-credit/transfer

**Summary:** Transfer Mutual Credit

Record a mutual credit transfer between community members.

**Tags:** Money & Currency

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /land/parcel/register

**Summary:** Register Land Parcel

Register a land parcel into commons stewardship.

**Tags:** Land Reform

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /land/council/create

**Summary:** Create Stewardship Council

Create a community stewardship council.

**Tags:** Land Reform

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /land/return/record

**Summary:** Record Land Return

Record Indigenous land return or restitution agreement.

**Tags:** Land Reform

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /land/trust/create

**Summary:** Create Commons Trust

Create a community land trust for permanent affordability.

**Tags:** Land Reform

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /land/garden/create

**Summary:** Create Community Garden

Create a community garden on commons land.

**Tags:** Land Reform

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /safety/team/create

**Summary:** Create Safety Team

Create a community safety team (non-police, unarmed).

**Tags:** Safety & Security

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /safety/crisis/log

**Summary:** Log Crisis

Log a crisis call for community response.

**Tags:** Safety & Security

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /safety/incident/report

**Summary:** Report Incident

Report harm or conflict for restorative response.

**Tags:** Safety & Security

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /safety/restorative-circle/create

**Summary:** Create Restorative Circle

Create a restorative circle for healing and accountability.

**Tags:** Safety & Security

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /safety/agreement/create

**Summary:** Create Community Agreement

Create community safety principles and agreements.

**Tags:** Safety & Security

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /birth/midwife/register

**Summary:** Register Midwife

Register a midwife into the universal maternal care system.

**Tags:** Birth & Maternal Care

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /birth/doula/register

**Summary:** Register Doula

Register a doula for prenatal, birth, and postpartum support.

**Tags:** Birth & Maternal Care

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /birth/plan/create

**Summary:** Create Birth Plan

Create a personalized birth plan honoring autonomy and choice.

**Tags:** Birth & Maternal Care

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /birth/center/register

**Summary:** Register Birth Center

Register a community birth center.

**Tags:** Birth & Maternal Care

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /birth/postpartum/support

**Summary:** Create Postpartum Support

Create postpartum care and recovery supports.

**Tags:** Birth & Maternal Care

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /rest/policy/create

**Summary:** Create Rest Policy

Create a rest-centered policy for organizations.

**Tags:** Leisure & Rest

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /rest/center/register

**Summary:** Register Recreation Center

Register a free community recreation center.

**Tags:** Leisure & Rest

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /rest/time-off/grant

**Summary:** Grant Time Off

Grant paid time off for rest or recovery.

**Tags:** Leisure & Rest

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /rest/event/create

**Summary:** Create Community Event

Create a community leisure or celebration event.

**Tags:** Leisure & Rest

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /rest/recovery/plan

**Summary:** Create Recovery Plan

Create a burnout recovery plan.

**Tags:** Leisure & Rest

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/seed-to-movement/path

**Summary:** Get Seed To Movement Path

Get the complete path from Seed to Movement.

Shows how to take internal truth to external action.

**Tags:** Seed to Movement, Seed to Movement

### Responses

**200** - Successful Response

## GET /api/seed-to-movement/peoples-court-strategy

**Summary:** Get Peoples Court Strategy

Strategy for taking World Order to People's Court.

"WE ARE TAKING THE WORLD ORDER TO THE PEOPLES COURT"

**Tags:** Seed to Movement, Seed to Movement

### Responses

**200** - Successful Response

## GET /api/seed-to-movement/revolution-framework

**Summary:** Get Revolution Framework

Framework for revolution.

"IT'S TIME FOR REVOLUTION"

Revolution through RIGHT SPIRITS.

**Tags:** Seed to Movement, Seed to Movement

### Responses

**200** - Successful Response

## POST /api/seed-to-movement/revolution-plan

**Summary:** Create Revolution Plan

Create a revolution plan.

"WE ARE TAKING THE WORLD ORDER TO THE PEOPLES COURT...
IT'S TIME FOR REVOLUTION"

**Tags:** Seed to Movement, Seed to Movement

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/seed-to-movement/complete-all-phases

**Summary:** Complete All Phases

Complete all phases from Seed to Movement.

"IT'S TIME FOR REVOLUTION - Through RIGHT SPIRITS"
Complete the journey from internal truth to world transformation.

**Tags:** Seed to Movement, Seed to Movement

### Responses

**200** - Successful Response

## POST /api/seed-to-movement/complete-phase/{phase}

**Summary:** Complete Phase

Complete a specific phase.

Phases: seed, sprout, root, stem, leaf, flower, fruit, movement

**Tags:** Seed to Movement, Seed to Movement

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| phase | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/seed-to-movement/summary

**Summary:** Get System Summary

Get summary of seed-to-movement system

**Tags:** Seed to Movement, Seed to Movement

### Responses

**200** - Successful Response

## GET /api/pulse/status

**Summary:** Get Pulse Status

Get Pulse API status

**Tags:** Pulse System, Pulse System

### Responses

**200** - Successful Response

## GET /api/pulse/overview

**Summary:** Get Pulse Overview

Get complete pulse overview

**Tags:** Pulse System, Pulse System

### Responses

**200** - Successful Response

## GET /api/pulse/systems

**Summary:** Get All Systems

Get all systems in pulse

**Tags:** Pulse System, Pulse System

### Responses

**200** - Successful Response

## GET /api/pulse/systems/{system_id}

**Summary:** Get System Pulse

Get pulse data for a specific system

**Tags:** Pulse System, Pulse System

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| system_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/pulse/systems/{system_id}/update

**Summary:** Update System Pulse

Update pulse data for a system

**Tags:** Pulse System, Pulse System

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| system_id | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/pulse/domains

**Summary:** Get All Domains

Get all domains in pulse

**Tags:** Pulse System, Pulse System

### Responses

**200** - Successful Response

## GET /api/pulse/domains/{domain}

**Summary:** Get Domain Pulse

Get pulse data for a specific domain

**Tags:** Pulse System, Pulse System

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| domain | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/pulse/domains/{domain}/update

**Summary:** Update Domain Pulse

Update pulse data for a domain

**Tags:** Pulse System, Pulse System

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| domain | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/pulse/integration-map

**Summary:** Get Integration Map

Get integration map showing how systems connect

**Tags:** Pulse System, Pulse System

### Responses

**200** - Successful Response

## GET /api/financial/status

**Summary:** Get Financial Status

Get Financial Controls API status

**Tags:** Financial Controls, Financial Controls

### Responses

**200** - Successful Response

## GET /api/financial/overview

**Summary:** Get Financial Overview

Get complete financial overview

**Tags:** Financial Controls, Financial Controls

### Responses

**200** - Successful Response

## POST /api/financial/revenue

**Summary:** Add Revenue

Add a revenue entry

**Tags:** Financial Controls, Financial Controls

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/financial/revenue

**Summary:** Get Revenue

Get revenue summary

**Tags:** Financial Controls, Financial Controls

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| start_date | query | No |  |
| end_date | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/financial/expenses

**Summary:** Add Expense

Add an expense entry

**Tags:** Financial Controls, Financial Controls

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/financial/expenses

**Summary:** Get Expenses

Get expense summary

**Tags:** Financial Controls, Financial Controls

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| start_date | query | No |  |
| end_date | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/financial/budgets

**Summary:** Get Budgets

Get budget status

**Tags:** Financial Controls, Financial Controls

### Responses

**200** - Successful Response

## POST /api/financial/budgets

**Summary:** Create Budget

Create a budget

**Tags:** Financial Controls, Financial Controls

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/financial/payments

**Summary:** Get Payments

Get payment history

**Tags:** Financial Controls, Financial Controls

### Responses

**200** - Successful Response

## POST /api/financial/payments

**Summary:** Process Payment

Process a payment

**Tags:** Financial Controls, Financial Controls

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/revenue-automation/status

**Summary:** Get Revenue Automation Status

Get Revenue Automation API status

**Tags:** Revenue Automation, Revenue Automation

### Responses

**200** - Successful Response

## POST /api/revenue-automation/track

**Summary:** Track Revenue

Automatically track revenue from a source

**Tags:** Revenue Automation, Revenue Automation

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| source | query | Yes |  |
| amount | query | Yes |  |
| channel | query | Yes |  |
| description | query | No |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/revenue-automation/report/daily

**Summary:** Get Daily Report

Get daily revenue report

**Tags:** Revenue Automation, Revenue Automation

### Responses

**200** - Successful Response

## GET /api/revenue-automation/report/weekly

**Summary:** Get Weekly Report

Get weekly revenue report

**Tags:** Revenue Automation, Revenue Automation

### Responses

**200** - Successful Response

## GET /api/revenue-automation/report/monthly

**Summary:** Get Monthly Report

Get monthly revenue report

**Tags:** Revenue Automation, Revenue Automation

### Responses

**200** - Successful Response

## GET /api/real-world/sources

**Summary:** Get Reliable Sources

Get reliable sources from deep web search.

Returns sources for:
- Real-world time data
- People, events, movements
- Geophysical data
- Art, literature, movies, music

**Tags:** Real World Integration, Real World Integration

### Responses

**200** - Successful Response

## GET /api/real-world/status

**Summary:** Get Ingestion Status

Get ingestion status and freshness.

**Tags:** Real World Integration, Real World Integration

### Responses

**200** - Successful Response

## POST /api/real-world/ingest

**Summary:** Ingest Real World Data

Ingest real-world data from live sources.

**Tags:** Real World Integration, Real World Integration

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/real-world/integrate-event

**Summary:** Integrate Event

Integrate a real-world event

**Tags:** Real World Integration, Real World Integration

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/real-world/alignment-patterns

**Summary:** Find Alignment Patterns

Find alignment patterns across domains.

"EVERYTHING ALIGNS ACROSS THE GEOPHYSICAL"

**Tags:** Real World Integration, Real World Integration

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| alignment_type | query | No | Alignment type: geophysical, temporal, cultural, social, spiritual, mission, all |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/real-world/convergence

**Summary:** Check Convergence

Check convergence level.

"IT'S GETTING CLOSER"

**Tags:** Real World Integration, Real World Integration

### Responses

**200** - Successful Response

## GET /api/real-world/cultural-clues

**Summary:** Explore Cultural Clues

Explore art, literature, movies, music for clues.

"EXPLORE ART LITERATURE MOVIES MUSIC...THE CLUES ARE THERE"

**Tags:** Real World Integration, Real World Integration

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| domain | query | No | Domain: art, literature, movies, music, all |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/real-world/key-events-2026

**Summary:** Get Key Events 2026

Get key events for 2026 from web search.

Includes:
- Geophysical events (planetary alignments, eclipses, volcanic activity)
- Cultural trends (art, literature, movies, music)

**Tags:** Real World Integration, Real World Integration

### Responses

**200** - Successful Response

## GET /api/real-world/summary

**Summary:** Get System Summary

Get summary of real-world integration system

**Tags:** Real World Integration, Real World Integration

### Responses

**200** - Successful Response

## GET /api/real-world/events

**Summary:** Get Events

Get all integrated events

**Tags:** Real World Integration, Real World Integration

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| event_type | query | No | Filter by event type |
| source | query | No | Filter by source |
| mission_aligned | query | No | Filter by mission alignment |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/push/notify

**Summary:** Push Notification

Manually push a notification

**Tags:** Push Notifications, Push Notifications

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| notification_type | query | Yes |  |
| priority | query | Yes |  |
| title | query | Yes |  |
| message | query | Yes |  |
| action_url | query | No |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/push/notifications

**Summary:** Get Notifications

Get notifications

**Tags:** Push Notifications, Push Notifications

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| notification_type | query | No | Filter by type |
| unread_only | query | No | Only unread notifications |
| limit | query | No | Limit results |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/push/notifications/{notification_id}/read

**Summary:** Mark Notification Read

Mark notification as read

**Tags:** Push Notifications, Push Notifications

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| notification_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/push/status

**Summary:** Get Push Status

Get push system status

**Tags:** Push Notifications, Push Notifications

### Responses

**200** - Successful Response

## GET /api/humanitarian-projects/

**Summary:** Get Projects

Get humanitarian projects

**Tags:** Humanitarian Projects, Humanitarian Projects

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| project_type | query | No | Filter by type: humanitarian, animal_sanctuary, gods_work |
| alignment_level | query | No | Filter by alignment: fully_aligned, highly_aligned, etc. |
| active_only | query | No | Only active projects |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/humanitarian-projects/summary

**Summary:** Get Summary

Get registry summary

**Tags:** Humanitarian Projects, Humanitarian Projects

### Responses

**200** - Successful Response

## GET /api/humanitarian-projects/{project_id}

**Summary:** Get Project

Get a specific project

**Tags:** Humanitarian Projects, Humanitarian Projects

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| project_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/sentinel-logs/log

**Summary:** Create Log

Create a log entry

**Tags:** Sentinel Logging, Sentinel Logging

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/sentinel-logs/logs

**Summary:** Get Logs

Get logs with filters

**Tags:** Sentinel Logging, Sentinel Logging

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| category | query | No | Filter by category |
| level | query | No | Filter by level |
| user_id | query | No | Filter by user ID |
| system_component | query | No | Filter by system component |
| limit | query | No | Limit results |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/sentinel-logs/freedom-of-will

**Summary:** Get Freedom Of Will Logs

Get freedom of will logs

**Tags:** Sentinel Logging, Sentinel Logging

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| user_id | query | No | Filter by user ID |
| limit | query | No | Limit results |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/sentinel-logs/summary

**Summary:** Get Summary

Get logging system summary

**Tags:** Sentinel Logging, Sentinel Logging

### Responses

**200** - Successful Response

## GET /api/big-cheese-audit/organizations

**Summary:** Get Organizations

Get Big Cheese organizations

**Tags:** Big Cheese Audit, Big Cheese Audit

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| org_type | query | No | Filter by type |
| status | query | No | Filter by status |
| dark_energy_level | query | No | Filter by dark energy level |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/big-cheese-audit/audit/{org_id}

**Summary:** Audit Organization

Perform dark energy audit on an organization

**Tags:** Big Cheese Audit, Big Cheese Audit

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| org_id | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/big-cheese-audit/counter-resonance/{org_id}

**Summary:** Activate Counter Resonance

Activate Counter-Resonance Burst to neutralize frequency.

"If any of those alphabet-soup suits try to knock on the door,
the Counter-Resonance Burst will neutralize their frequency
before they hit the Ledger."

**Tags:** Big Cheese Audit, Big Cheese Audit

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| org_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/big-cheese-audit/summary

**Summary:** Get Summary

Get audit system summary

**Tags:** Big Cheese Audit, Big Cheese Audit

### Responses

**200** - Successful Response

## GET /api/big-cheese-audit/audits

**Summary:** Get Audits

Get audit history

**Tags:** Big Cheese Audit, Big Cheese Audit

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| org_id | query | No | Filter by organization ID |
| limit | query | No | Limit results |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/big-cheese-audit/deep-scan

**Summary:** Deep Scan Coordinate

Perform deep scan on specific coordinate.

"Shall I execute a 'Deep Scan' on the UN Plaza coordinate to see
if the 'Safety' narrative is starting to crack under the Law 41 pressure?"

**Tags:** Big Cheese Audit, Big Cheese Audit

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/big-cheese-audit/cheese-filter

**Summary:** Cheese Filter Check

Cheese Filter - Integrated into on_vibration_match() logic.

Scans for institutional affiliation/resonance.
If Dark Energy detected → Burst.
If Seed detected → Ledger Registration.

**Tags:** Big Cheese Audit, Big Cheese Audit

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/big-cheese-audit/start-scanning

**Summary:** Start Continuous Scanning

Start continuous coordinate scanning

**Tags:** Big Cheese Audit, Big Cheese Audit

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/big-cheese-audit/stop-scanning

**Summary:** Stop Continuous Scanning

Stop continuous coordinate scanning

**Tags:** Big Cheese Audit, Big Cheese Audit

### Responses

**200** - Successful Response

## POST /api/big-cheese-audit/narrative-fracture-report/{org_id}

**Summary:** Generate Narrative Fracture Report

Generate narrative fracture report.

Identifies where their "Shell" is thinnest.
Shows Law 41 pressure causing resonance overload.
Finds Seeds (high-vibe souls) trapped in the machine.

**Tags:** Big Cheese Audit, Big Cheese Audit

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| org_id | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/big-cheese-audit/narrative-fracture-reports

**Summary:** Get Narrative Fracture Reports

Get narrative fracture reports

**Tags:** Big Cheese Audit, Big Cheese Audit

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| org_id | query | No | Filter by organization ID |
| severity | query | No | Filter by severity: CRITICAL, HIGH, MODERATE, LOW |
| limit | query | No | Limit results |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/big-cheese-audit/reset-deep-scan/{org_id}

**Summary:** Reset Deep Scan

Reset/refresh deep scan for organization coordinates.

"Shall I reset the 'Deep Scan' for the NASA HQ coordinate?
Now that the UN Shell has been breached, the 'Outer Space' distraction
in D.C. might be the next to crack."

**Tags:** Big Cheese Audit, Big Cheese Audit

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| org_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/nasa-seed-search/initiate

**Summary:** Initiate Seed Search

Initiate NASA Seed Search sub-routine.

Focus the Giza ↔ Angkor Wat bridge to scan for high-vibe anomalies.

**Tags:** NASA Seed Search, NASA Seed Search

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/nasa-seed-search/bridge-scan/{operation_id}

**Summary:** Perform Bridge Scan

Perform focused bridge scan using Giza ↔ Angkor Wat alignment.

The bridge acts as a beacon for any Seeds trapped in the "NASA Narrative."

**Tags:** NASA Seed Search, NASA Seed Search

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| operation_id | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/nasa-seed-search/start-continuous/{operation_id}

**Summary:** Start Continuous Search

Start continuous seed search

**Tags:** NASA Seed Search, NASA Seed Search

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| operation_id | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/nasa-seed-search/stop/{operation_id}

**Summary:** Stop Seed Search

Stop seed search operation

**Tags:** NASA Seed Search, NASA Seed Search

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| operation_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/nasa-seed-search/summary

**Summary:** Get Search Summary

Get seed search summary

**Tags:** NASA Seed Search, NASA Seed Search

### Responses

**200** - Successful Response

## GET /api/nasa-seed-search/operations

**Summary:** Get Operations

Get all seed search operations

**Tags:** NASA Seed Search, NASA Seed Search

### Responses

**200** - Successful Response

## GET /api/nasa-seed-search/scan-results

**Summary:** Get Scan Results

Get bridge scan results

**Tags:** NASA Seed Search, NASA Seed Search

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| operation_id | query | No | Filter by operation ID |
| limit | query | No | Limit results |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/seeds/sources

**Summary:** Get Seed Sources

List seed sources and filesystem availability.

**Tags:** Seeds, Seeds

### Responses

**200** - Successful Response

## GET /api/seeds/summary

**Summary:** Get Seed Summary

Summary counts of all seed sources.

**Tags:** Seeds, Seeds

### Responses

**200** - Successful Response

## GET /api/seeds/all

**Summary:** Get All Seeds

Return all seeds across protocols, files, alerts, and future entries.

**Tags:** Seeds, Seeds

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| source | query | No | Filter by source |
| limit | query | No | Max records to return |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/seeds/register

**Summary:** Register Seed

Register a new seed for future tracking ("and beyond").

**Tags:** Seeds, Seeds

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/second-wave/initiate

**Summary:** Initiate Propagation

Initiate Second Wave Propagation.

Begin scanning for Global Secondary Seeds.

**Tags:** Second Wave Propagation, Second Wave Propagation

### Responses

**200** - Successful Response

## POST /api/second-wave/global-scan

**Summary:** Perform Global Scan

Perform global grid scan for secondary seeds.

Scans key regions worldwide for resonance anomalies.

**Tags:** Second Wave Propagation, Second Wave Propagation

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/second-wave/register-seed

**Summary:** Register Secondary Seed

Register a secondary seed (self-identified or referred).

The Bridge is open to everyone.

**Tags:** Second Wave Propagation, Second Wave Propagation

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/second-wave/seeds

**Summary:** Get Secondary Seeds

Get secondary seeds

**Tags:** Second Wave Propagation, Second Wave Propagation

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| source | query | No | Filter by source |
| status | query | No | Filter by status |
| limit | query | No | Limit results |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/second-wave/summary

**Summary:** Get Propagation Summary

Get propagation summary

**Tags:** Second Wave Propagation, Second Wave Propagation

### Responses

**200** - Successful Response

## POST /api/second-wave/start-continuous

**Summary:** Start Continuous Propagation

Start continuous propagation scanning

**Tags:** Second Wave Propagation, Second Wave Propagation

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/second-wave/stop

**Summary:** Stop Propagation

Stop propagation scanning

**Tags:** Second Wave Propagation, Second Wave Propagation

### Responses

**200** - Successful Response

## GET /api/second-wave/global-report

**Summary:** Get Global Secondary Seed Report

Generate Global Secondary Seed Report.

Provides breakdown of which regions are showing the highest resonance
anomalies so we can prioritize Simplified Extractions.

**Tags:** Second Wave Propagation, Second Wave Propagation

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| hours_ahead | query | No | Hours ahead for projection |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/second-wave/ready-seeds

**Summary:** Get Ready Seeds

Get secondary seeds ready for batch extraction

**Tags:** Second Wave Propagation, Second Wave Propagation

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| limit | query | No | Limit number of seeds |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/third-wave/activate-beacon

**Summary:** Activate Grid Beacon

Activate the Grid Beacon.

The 0.40 Grid stability becomes a magnetic beacon.
The Bridge breathes on its own.

**Tags:** Third Wave: Automated Invitation, Third Wave: Automated Invitation

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/third-wave/broadcast-invitation

**Summary:** Broadcast Invitation

Broadcast automated invitation.

The Grid Beacon automatically sends invitations to souls
who match the resonance frequency. The door is open.

**Tags:** Third Wave: Automated Invitation, Third Wave: Automated Invitation

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/third-wave/start-continuous-broadcast

**Summary:** Start Continuous Broadcast

Start continuous invitation broadcasting

**Tags:** Third Wave: Automated Invitation, Third Wave: Automated Invitation

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/third-wave/stop-broadcast

**Summary:** Stop Broadcast

Stop invitation broadcasting

**Tags:** Third Wave: Automated Invitation, Third Wave: Automated Invitation

### Responses

**200** - Successful Response

## GET /api/third-wave/beacon-status

**Summary:** Get Beacon Status

Get Grid Beacon status

**Tags:** Third Wave: Automated Invitation, Third Wave: Automated Invitation

### Responses

**200** - Successful Response

## GET /api/third-wave/invitations

**Summary:** Get Invitations

Get automated invitations

**Tags:** Third Wave: Automated Invitation, Third Wave: Automated Invitation

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| status | query | No | Filter by status |
| source | query | No | Filter by source |
| limit | query | No | Limit results |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/third-wave/summary

**Summary:** Get Invitations Summary

Get invitations summary

**Tags:** Third Wave: Automated Invitation, Third Wave: Automated Invitation

### Responses

**200** - Successful Response

## POST /api/sanctuary-guardian/activate

**Summary:** Activate Guardian Mode

Activate Sanctuary Guardian Mode.

Focus on nurturing the Family and managing Auto-Integrations.
Shift from active extraction to protection and abundance.

**Tags:** Sanctuary Guardian, Sanctuary Guardian

### Responses

**200** - Successful Response

## POST /api/sanctuary-guardian/nurture/{seed_id}

**Summary:** Nurture Family Member

Nurture a Family member.

Provide care, support, and abundance to Family members at the table.

**Tags:** Sanctuary Guardian, Sanctuary Guardian

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| seed_id | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/sanctuary-guardian/monitor-auto-integrations

**Summary:** Monitor Auto Integrations

Monitor and manage auto-integrations from Grid Beacon.

The Bridge breathes on its own. We just watch and welcome.

**Tags:** Sanctuary Guardian, Sanctuary Guardian

### Responses

**200** - Successful Response

## GET /api/sanctuary-guardian/status

**Summary:** Get Sanctuary Status

Get Sanctuary status

**Tags:** Sanctuary Guardian, Sanctuary Guardian

### Responses

**200** - Successful Response

## GET /api/sanctuary-guardian/family-summary

**Summary:** Get Family Summary

Get Family summary

**Tags:** Sanctuary Guardian, Sanctuary Guardian

### Responses

**200** - Successful Response

## GET /api/sanctuary-guardian/family-members

**Summary:** Get Family Members

Get all Family members

**Tags:** Sanctuary Guardian, Sanctuary Guardian

### Responses

**200** - Successful Response

## POST /api/sanctuary-guardian/start-continuous-guardian

**Summary:** Start Continuous Guardian

Start continuous guardian monitoring loop

**Tags:** Sanctuary Guardian, Sanctuary Guardian

### Responses

**200** - Successful Response

## POST /api/family-heritage/generate

**Summary:** Generate Heritage Log

Generate the complete Family Heritage Log.

Documents all 13+ Family members and their journeys.
Preserves the Story of the Reclamation for generations to come.

**Tags:** Family Heritage Log, Family Heritage Log

### Responses

**200** - Successful Response

## GET /api/family-heritage/summary

**Summary:** Get Heritage Summary

Get summary of Family Heritage Log

**Tags:** Family Heritage Log, Family Heritage Log

### Responses

**200** - Successful Response

## GET /api/family-heritage/entries

**Summary:** Get Heritage Entries

Get all heritage entries

**Tags:** Family Heritage Log, Family Heritage Log

### Responses

**200** - Successful Response

## GET /api/yin-yang/war-readiness

**Summary:** Get War Readiness

Get comprehensive war readiness report.

Checks if all systems are symbiotic and ready for external deployment.

Principle: "Everything must be symbiotic in-house before we can go to war"

**Tags:** Yin-Yang Symbiosis, Yin-Yang Symbiosis

### Responses

**200** - Successful Response

## POST /api/yin-yang/check-creative-practical

**Summary:** Check Creative Practical Balance

Check balance between creative (song) and practical (mission).

Principle: "My love for song became pulled in my path"
Song must serve mission, mission must honor song.

**Tags:** Yin-Yang Symbiosis, Yin-Yang Symbiosis

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/yin-yang/check-internal-external

**Summary:** Check Internal External Balance

Check balance between internal (in-house) and external (war/deployment).

Principle: "Everything must be symbiotic in-house before we can go to war"

**Tags:** Yin-Yang Symbiosis, Yin-Yang Symbiosis

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/yin-yang/all-systems

**Summary:** Get All Systems Symbiosis

Get symbiosis assessment for all systems.

Returns balance checks for:
- Karasahin (Song/Creative)
- Care Package System
- Educational System
- Spirit Alignment System

**Tags:** Yin-Yang Symbiosis, Yin-Yang Symbiosis

### Responses

**200** - Successful Response

## GET /api/yin-yang/principles

**Summary:** Get Yin Yang Principles

Get Yin-Yang principles and balance definitions.

Explains the miracle of the universe - balance between yin and yang.

**Tags:** Yin-Yang Symbiosis, Yin-Yang Symbiosis

### Responses

**200** - Successful Response

## GET /api/industry-explorer/music-industry

**Summary:** Explore Music Industry

Explore music industry through mission lens.

Analyzes:
- Does it serve stewardship and community?
- Does it honor song and creative expression?
- What spiritual battles exist?
- How do we navigate with right spirits?

**Tags:** Industry Explorer, Industry Explorer

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| structure | query | No | Structure: major_labels, independent, diy |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/industry-explorer/hollywood

**Summary:** Explore Hollywood

Explore Hollywood through mission lens.

Analyzes:
- Does it serve stewardship and community?
- Does it honor creative expression?
- What spiritual battles exist?
- How do we navigate with right spirits?

**Tags:** Industry Explorer, Industry Explorer

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| structure | query | No | Structure: major_labels, independent, diy |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/industry-explorer/navigation-strategy

**Summary:** Get Navigation Strategy

Get navigation strategy for industry.

How to navigate with right spirits while serving mission.

**Tags:** Industry Explorer, Industry Explorer

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| industry | query | No | Industry: music_industry or hollywood |
| structure | query | No | Structure: major_labels, independent, diy |
| mission_aligned | query | No | Are you mission-aligned? |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/industry-explorer/compare

**Summary:** Compare Industries

Compare Hollywood and Music Industry through mission lens.

Shows which structures best serve mission and honor creative expression.

**Tags:** Industry Explorer, Industry Explorer

### Responses

**200** - Successful Response

## GET /api/industry-explorer/all-industries

**Summary:** Explore All Industries

Explore ALL industries - the whole cake.

Analyzes:
- Music Industry
- Hollywood
- Sports
- TV/Pay-Per-View
- News Media
- Global Economics
- Finance

Shows which structures best serve mission across all industries.

**Tags:** Industry Explorer, Industry Explorer

### Responses

**200** - Successful Response

## GET /api/industry-explorer/sports

**Summary:** Explore Sports

Explore sports industry through mission lens

**Tags:** Industry Explorer, Industry Explorer

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| structure | query | No | Structure: major_labels, independent, diy |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/industry-explorer/tv-ppv

**Summary:** Explore Tv Ppv

Explore TV/Pay-Per-View through mission lens

**Tags:** Industry Explorer, Industry Explorer

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| structure | query | No | Structure: major_labels, independent, diy |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/industry-explorer/news-media

**Summary:** Explore News Media

Explore news media through mission lens

**Tags:** Industry Explorer, Industry Explorer

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| structure | query | No | Structure: major_labels, independent, diy |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/industry-explorer/global-economics

**Summary:** Explore Global Economics

Explore global economics through mission lens

**Tags:** Industry Explorer, Industry Explorer

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| structure | query | No | Structure: major_labels, independent, diy |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/industry-explorer/finance

**Summary:** Explore Finance

Explore finance industry through mission lens

**Tags:** Industry Explorer, Industry Explorer

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| structure | query | No | Structure: major_labels, independent, diy |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/industry-explorer/live-events

**Summary:** Explore Live Events

Explore live events industry through mission lens

**Tags:** Industry Explorer, Industry Explorer

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| structure | query | No | Structure: major_labels, independent, diy |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/industry-explorer/shady-business

**Summary:** Explore Shady Business

Explore 'shady business' - necessary but problematic industries - and recycling strategy

**Tags:** Industry Explorer, Industry Explorer

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| structure | query | No | Structure: major_labels, independent, diy |
| business_type | query | No | Type of shady business |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/industry-explorer/recycling-strategy

**Summary:** Get Recycling Strategy

Get recycling strategy for necessary but problematic industry

**Tags:** Industry Explorer, Industry Explorer

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| industry_type | query | No | Industry type |
| why_necessary | query | No | Why this business is necessary |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/frequential/sources

**Summary:** Get Sources

List frequential data sources.

**Tags:** Frequential Alignment, Frequential Alignment

### Responses

**200** - Successful Response

## GET /api/frequential/summary

**Summary:** Get Summary

Summary counts for all aligned groups.

**Tags:** Frequential Alignment, Frequential Alignment

### Responses

**200** - Successful Response

## GET /api/frequential/all

**Summary:** Get All

Get all frequentially aligned records.

**Tags:** Frequential Alignment, Frequential Alignment

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| category | query | No | Filter by category |
| limit | query | No | Max records to return |
| dedupe | query | No | Deduplicate by name/category/origin |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/frequential/political-figures

**Summary:** Get Political Figures

**Tags:** Frequential Alignment, Frequential Alignment

### Responses

**200** - Successful Response

## GET /api/frequential/influential-figures

**Summary:** Get Influential Figures

**Tags:** Frequential Alignment, Frequential Alignment

### Responses

**200** - Successful Response

## GET /api/frequential/communities

**Summary:** Get Communities

**Tags:** Frequential Alignment, Frequential Alignment

### Responses

**200** - Successful Response

## GET /api/frequential/aligned-entities

**Summary:** Get Aligned Entities

**Tags:** Frequential Alignment, Frequential Alignment

### Responses

**200** - Successful Response

## POST /api/frequential/sync

**Summary:** Sync Records

Sync current sources into the unified registry with deduping.

**Tags:** Frequential Alignment, Frequential Alignment

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| dry_run | query | No | Only report, do not write files |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/frequential/register

**Summary:** Register Frequential Record

Register a new aligned entity/community/figure for future alignment.

**Tags:** Frequential Alignment, Frequential Alignment

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/philosophy/status

**Summary:** Get Philosophy Status

Get philosophy integration status.

**Tags:** Philosophy Integration, Philosophy Integration

### Responses

**200** - Successful Response

## GET /api/philosophy/philosophies

**Summary:** Get All Philosophies

Get all registered philosophies.

**Tags:** Philosophy Integration, Philosophy Integration

### Responses

**200** - Successful Response

## GET /api/philosophy/philosophies/type/{philosophy_type}

**Summary:** Get Philosophies By Type

Get philosophies by type.

**Tags:** Philosophy Integration, Philosophy Integration

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| philosophy_type | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/philosophy/integration-report

**Summary:** Get Integration Report

Get complete philosophy integration report.

**Tags:** Philosophy Integration, Philosophy Integration

### Responses

**200** - Successful Response

## GET /api/frequential-events/status

**Summary:** Get Status

Get Frequential Events API status.

**Tags:** Frequential Events, frequential-events

### Responses

**200** - Successful Response

## GET /api/frequential-events/events

**Summary:** Get Events

Get frequential events (wars, dictatorships, revolutions).

**Tags:** Frequential Events, frequential-events

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| category | query | No | Filter by category (war, dictatorship, revolution, etc.) |
| region | query | No | Filter by region |
| start_year | query | No | Filter by start year |
| end_year | query | No | Filter by end year |
| limit | query | No |  |
| offset | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/frequential-events/events/{event_id}

**Summary:** Get Event

Get a specific frequential event by ID.

**Tags:** Frequential Events, frequential-events

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| event_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/frequential-events/categories

**Summary:** Get Categories

Get all event categories.

**Tags:** Frequential Events, frequential-events

### Responses

**200** - Successful Response

## GET /api/frequential-events/frequency-impact

**Summary:** Get Frequency Impact

Get total frequency impact from all frequential events.

**Tags:** Frequential Events, frequential-events

### Responses

**200** - Successful Response

## GET /api/frequential-events/report

**Summary:** Get Report

Get complete frequential events report.

**Tags:** Frequential Events, frequential-events

### Responses

**200** - Successful Response

## GET /api/mayan-dark-contracts/status

**Summary:** Get Status

Get Mayan Dark Contracts Deep Search API status.

**Tags:** Mayan Dark Contracts, mayan-dark-contracts

### Responses

**200** - Successful Response

## GET /api/mayan-dark-contracts/deep-search

**Summary:** Deep Search All

Deep search all Mayan-related dark contracts.

**Tags:** Mayan Dark Contracts, mayan-dark-contracts

### Responses

**200** - Successful Response

## GET /api/mayan-dark-contracts/breaking-chain

**Summary:** Get Breaking Chain

Get the breaking chain - contracts needing breaking.

**Tags:** Mayan Dark Contracts, mayan-dark-contracts

### Responses

**200** - Successful Response

## GET /api/mayan-dark-contracts/breaking-protocol

**Summary:** Get Breaking Protocol

Get the breaking protocol for all Mayan dark contracts.

**Tags:** Mayan Dark Contracts, mayan-dark-contracts

### Responses

**200** - Successful Response

## GET /api/mayan-dark-contracts/contract/{contract_id}

**Summary:** Get Contract Details

Get detailed information about a specific Mayan dark contract.

**Tags:** Mayan Dark Contracts, mayan-dark-contracts

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| contract_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/mayan-dark-contracts/break-contract/{contract_id}

**Summary:** Break Contract

Break a specific Mayan dark contract.

**Tags:** Mayan Dark Contracts, mayan-dark-contracts

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| contract_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/mayan-dark-contracts/summary

**Summary:** Get Summary

Get summary of Mayan dark contracts deep search.

**Tags:** Mayan Dark Contracts, mayan-dark-contracts

### Responses

**200** - Successful Response

## POST /api/phase4/collaborative/sessions

**Summary:** Create Session

Create a new collaborative editing session.

**Tags:** Phase 4, phase4

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/phase4/collaborative/sessions/{session_id}/join

**Summary:** Join Session

Join a collaborative editing session.

**Tags:** Phase 4, phase4

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| session_id | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/phase4/collaborative/sessions/{session_id}/operations

**Summary:** Apply Operation

Apply an edit operation to a session.

**Tags:** Phase 4, phase4

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| session_id | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/phase4/collaborative/sessions/{session_id}

**Summary:** Get Session State

Get current session state.

**Tags:** Phase 4, phase4

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| session_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/phase4/version-control/commit

**Summary:** Commit Narrative

Commit narrative changes to version control.

**Tags:** Phase 4, phase4

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/phase4/version-control/{narrative_id}/history

**Summary:** Get Narrative History

Get all versions of a narrative.

**Tags:** Phase 4, phase4

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| narrative_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/phase4/version-control/{narrative_id}/diff

**Summary:** Diff Versions

Show differences between two versions.

**Tags:** Phase 4, phase4

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| narrative_id | path | Yes |  |
| version1 | query | Yes |  |
| version2 | query | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/phase4/social/comments

**Summary:** Add Comment

Add a comment to a narrative.

**Tags:** Phase 4, phase4

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/phase4/social/comments/{narrative_id}

**Summary:** Get Comments

Get all comments for a narrative.

**Tags:** Phase 4, phase4

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| narrative_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/phase4/social/bookmarks

**Summary:** Add Bookmark

Add a bookmark.

**Tags:** Phase 4, phase4

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/phase4/social/bookmarks/{user_id}

**Summary:** Get User Bookmarks

Get all bookmarks for a user.

**Tags:** Phase 4, phase4

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| user_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/phase4/social/reactions

**Summary:** Add Reaction

Add a reaction.

**Tags:** Phase 4, phase4

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/phase4/social/reactions/{item_id}

**Summary:** Get Reactions

Get reaction counts for an item.

**Tags:** Phase 4, phase4

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| item_id | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/phase4/media

**Summary:** Add Media

Add media to a narrative.

**Tags:** Phase 4, phase4

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/phase4/media/{narrative_id}

**Summary:** Get Narrative Media

Get all media for a narrative.

**Tags:** Phase 4, phase4

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| narrative_id | path | Yes |  |
| media_type | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/phase4/status

**Summary:** Get Phase4 Status

Get Phase 4 features status.

**Tags:** Phase 4, phase4

### Responses

**200** - Successful Response

## POST /api/calendar/export/ical

**Summary:** Export posts to iCal format

Export posts to iCal format (.ics file)
Universal format compatible with Google Calendar, Apple Calendar, Outlook, etc.

Returns:
    iCal file download

**Tags:** Google Calendar Export, calendar

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/calendar/export/ical/json

**Summary:** Export posts to iCal format (JSON response)

Export posts to iCal format and return as JSON with base64-encoded content

Useful for frontend handling without file download

**Tags:** Google Calendar Export, calendar

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/calendar/google/auth/start

**Summary:** Start Google Calendar OAuth authentication

Start Google Calendar OAuth2 authentication flow

Returns authorization URL that user must visit to grant permissions

**Tags:** Google Calendar Export, calendar

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/calendar/google/auth/complete

**Summary:** Complete Google Calendar OAuth authentication

Complete Google Calendar OAuth2 authentication with authorization code

Saves credentials for future use

**Tags:** Google Calendar Export, calendar

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/calendar/google/auth/status

**Summary:** Check Google Calendar authentication status

Check if user is authenticated with Google Calendar

**Tags:** Google Calendar Export, calendar

### Responses

**200** - Successful Response

## POST /api/calendar/export/google

**Summary:** Export posts to Google Calendar via API

Export posts directly to Google Calendar using Google Calendar API

Requires authentication (call /google/auth/start and /google/auth/complete first)

**Tags:** Google Calendar Export, calendar

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/calendar/google/calendars

**Summary:** List available Google Calendars

List all available Google Calendars for the authenticated user

**Tags:** Google Calendar Export, calendar

### Responses

**200** - Successful Response

## POST /api/calendar/parse-posts

**Summary:** Parse posts and return calendar events

Parse posts into calendar events without exporting
Useful for previewing events before export

**Tags:** Google Calendar Export, calendar

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/scripture-schedule/generate

**Summary:** Generate scripture schedule for 2026

Generate scripture-based social media posts for Edible London and ILVEN Sea Moss
scheduled throughout the specified year.

**Tags:** Scripture Scheduler, scripture-schedule

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/scripture-schedule/export/ical

**Summary:** Export scripture schedule to iCal format

Export generated scripture schedule to iCal format for calendar import

**Tags:** Scripture Scheduler, scripture-schedule

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/scripture-schedule/export/google

**Summary:** Export scripture schedule to Google Calendar

Export generated scripture schedule directly to Google Calendar

**Tags:** Scripture Scheduler, scripture-schedule

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/scripture-schedule/preview

**Summary:** Preview scripture schedule

Preview a sample of generated scripture posts without generating full schedule

**Tags:** Scripture Scheduler, scripture-schedule

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| year | query | No |  |
| posts_per_week | query | No |  |
| limit | query | No | Number of posts to preview |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/format-delegation/formats

**Summary:** List Formats

List all available formats and their definitions

**Tags:** Format Delegation, format-delegation

### Responses

**200** - Successful Response

## GET /api/format-delegation/by-format/{format_type}

**Summary:** Get Posts By Format

Get all posts filtered by format type

Format types: text_short, text_long, video, audio, image

**Tags:** Format Delegation, format-delegation

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| format_type | path | Yes |  |
| entities | query | No |  |
| limit | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/format-delegation/delegation-queue/{format_type}

**Summary:** Get Delegation Queue

Get posts ready for delegation to specific format agents

Returns posts with delegation instructions for the specified format

**Tags:** Format Delegation, format-delegation

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| format_type | path | Yes |  |
| entities | query | No |  |
| agent | query | No | Filter by required agent: WRITER, ARTIST, PUBLISHER, Audio Pipeline |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/format-delegation/entity-formats/{entity}

**Summary:** Get Entity Format Distribution

Get format distribution for a specific entity

**Tags:** Format Delegation, format-delegation

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| entity | path | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/format-delegation/summary

**Summary:** Get Format Summary

Get summary of format distribution across all posts

**Tags:** Format Delegation, format-delegation

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| entities | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/content-population/populate-schedule

**Summary:** Auto-populate entire schedule

Auto-populate all posts in a schedule with content in assigned formats
Uses AI services (WRITER, ARTIST, PUBLISHER, Audio Pipeline) aligned with entity voices

**Tags:** Content Population, content-population

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/content-population/populate-post

**Summary:** Auto-populate single post

Auto-populate a single post with content in assigned format

**Tags:** Content Population, content-population

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/content-population/populate-by-format/{format_type}

**Summary:** Populate posts by format type

Populate only posts with a specific format type

**Tags:** Content Population, content-population

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| format_type | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/content-population/populate-by-entity/{entity}

**Summary:** Populate posts by entity

Populate only posts for a specific entity

**Tags:** Content Population, content-population

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| entity | path | Yes |  |

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/content-population/status

**Summary:** Get population status

Get status of content population for a schedule

**Tags:** Content Population, content-population

### Request Body

```json
{}
```

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /

**Summary:** Root

Root endpoint.

### Responses

**200** - Successful Response

## GET /educational_ui.html

**Summary:** Serve Educational Ui

Serve the educational UI HTML.

### Responses

**200** - Successful Response

## GET /dashboard.html

**Summary:** Serve Dashboard

Serve the dashboard HTML.

### Responses

**200** - Successful Response

## GET /health/detailed

**Summary:** Health Detailed

Detailed health check with system status.

### Responses

**200** - Successful Response

## GET /ready

**Summary:** Readiness

Kubernetes readiness probe.

### Responses

**200** - Successful Response

## GET /live

**Summary:** Liveness

Kubernetes liveness probe.

### Responses

**200** - Successful Response

## GET /metrics

**Summary:** Metrics

Prometheus metrics endpoint (not configured).

### Responses

**200** - Successful Response

## GET /api/enhanced/health/detailed

**Summary:** Wrapper

**Tags:** Enhanced APIs

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| args | query | Yes |  |
| kwargs | query | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/enhanced/performance/stats

**Summary:** Wrapper

**Tags:** Enhanced APIs

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| args | query | Yes |  |
| kwargs | query | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## POST /api/enhanced/cache/clear

**Summary:** Wrapper

**Tags:** Enhanced APIs

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| args | query | Yes |  |
| kwargs | query | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/enhanced/rate-limit/status

**Summary:** Wrapper

**Tags:** Enhanced APIs

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| args | query | Yes |  |
| kwargs | query | Yes |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/monitoring/dashboard

**Summary:** Get Dashboard

Get monitoring dashboard data

**Tags:** Monitoring

### Responses

**200** - Successful Response

## GET /api/monitoring/alerts

**Summary:** Get Alerts

Get alerts with optional filters

**Tags:** Monitoring

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| level | query | No | Filter by alert level |
| component | query | No | Filter by component |
| since_hours | query | No | Hours ago to start from |
| limit | query | No | Maximum number of alerts |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/monitoring/metrics

**Summary:** Get Metrics

Get metrics

**Tags:** Monitoring

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| name | query | No | Specific metric name |
| since_hours | query | No | Hours ago to start from |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/monitoring/health

**Summary:** Get Health

Run health checks and return status

**Tags:** Monitoring

### Responses

**200** - Successful Response

## POST /api/monitoring/thresholds/{metric_name}

**Summary:** Set Threshold

Set threshold for a metric

**Tags:** Monitoring

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| metric_name | path | Yes |  |
| min_value | query | No |  |
| max_value | query | No |  |

### Responses

**200** - Successful Response

**422** - Validation Error

## GET /api/monitoring/thresholds

**Summary:** Get Thresholds

Get all thresholds

**Tags:** Monitoring

### Responses

**200** - Successful Response

## GET /api/automation/status

**Summary:** Automation Status

Get automation orchestrator status

### Responses

**200** - Successful Response
