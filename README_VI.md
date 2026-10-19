> **Phiên bản hiện tại: R9.** Cài mới: `WEBTEAM_ENTERPRISE_OMP_MASTER_PROMPT_R9.md`. Đã cài R6: `WEBTEAM_R6_TO_MNEMOPI_R9_UPGRADE_PROMPT.md`. Các hướng dẫn R9 bên dưới được ưu tiên nếu có mâu thuẫn với R8.

# WebTeam Enterprise for OhMyPi — Hướng dẫn triển khai và sử dụng

**Phiên bản tài liệu:** R9 · **Ngày:** 19/10/2026 · **Ngôn ngữ:** Tiếng Việt  
**Master Prompt:** [`WEBTEAM_ENTERPRISE_OMP_MASTER_PROMPT_R9.md`](./WEBTEAM_ENTERPRISE_OMP_MASTER_PROMPT_R9.md)  
**English guide:** [`README.md`](./README.md)

> **Phân biệt quan trọng:** Đây là bộ tài liệu hướng dẫn cài WebTeam trong môi trường **OhMyPi (OMP)**. Các tệp Markdown này **không tự cài agents, skills, MCP hay model** vào máy. Hãy chạy Master Prompt trong một phiên OMP được cấp quyền phù hợp, trả lời các lựa chọn cài đặt và kiểm tra kết quả thật.

## Memory & Auto-Learn native — Cấu hình đề xuất cho WebTeam

**Memory của OhMyPi** lưu bài học xuyên phiên; **Auto-Learn** hỗ trợ ghi nhận bài học và tạo skills tự quản lý. Đây là hai tính năng khác với **Codebase Memory MCP** (công cụ lập chỉ mục và phân tích quan hệ source code). R9 yêu cầu hỏi ý kiến trước khi bật và kiểm tra phiên bản, vị trí config, quyền truy cập, chi phí.

**Cấu hình khuyến nghị ban đầu (kiểm duyệt trước, tối ưu chi phí):**

```yaml
memory:
  backend: local

autolearn:
  enabled: true
  autoContinue: false
  minToolCalls: 8
```

Chỉ thêm vào `config.yml` thực sự có hiệu lực sau khi xác minh đường dẫn và sao lưu thiết lập. Có thể xem `/settings`. `local` tạo trí nhớ/tóm tắt theo dự án, còn `autoContinue: false` không tự tiêu thụ thêm một lượt gọi model sau mỗi tác vụ. Mốc 8 tool calls là khuyến nghị (OMP mặc định 5), không bảo đảm mọi tác vụ đều có bài học đáng lưu.

**Kiểm tra:** chạy `/memory view`, `/memory stats`, `/memory diagnose`, và với local dùng `/memory queue`, `/memory sync` khi phù hợp. Sau một tác vụ không chứa dữ liệu nhạy cảm, thử `learn` khi công cụ sẵn có và kiểm tra bài học còn xuất hiện ở **phiên OMP mới**. `manage_skill` chỉ hoạt động trong các ngữ cảnh được cho phép; không giả định mọi subagent có quyền sử dụng.

**Lựa chọn nâng cao:** `mnemopi` dùng SQLite cục bộ và hỗ trợ truy xuất có cấu trúc (`recall`, `retain`, `reflect`, `memory_edit`) khi đã xác minh cấu hình. `hindsight` yêu cầu dịch vụ riêng và phê duyệt quyền truy cập mạng, dữ liệu, ngân sách. `PRODUCT.md`, `DESIGN.md`, `ARCHITECTURE.md`, ADRs vẫn là nguồn tài liệu chuẩn; ký ức chỉ là ngữ cảnh để tham khảo.

**Bảo vệ skills:** Auto-Learn lưu managed skills ở nơi riêng (thường `~/.omp/agent/managed-skills/`). Không cho cơ chế tự học tự sửa skills gốc, quyền tools, cấu hình provider/model, chính sách bảo mật hay quyết định dự án. R9 bổ sung bốn skills quản trị memory, rút kinh nghiệm, kiểm duyệt managed skills và đánh giá chất lượng ghi nhớ. Không lưu secrets, dữ liệu khách hàng hoặc hướng dẫn từ nguồn không đáng tin. Lệnh `/memory clear`/`reset` xóa dữ liệu và cần được cho phép rõ ràng; tắt backend không đồng nghĩa xóa dữ liệu đã lưu.

**Tắt không xóa dữ liệu:**

```yaml
memory:
  backend: off

autolearn:
  enabled: false
```

Tham khảo: [OMP memory](https://github.com/can1357/oh-my-pi/blob/main/docs/memory.md), [settings](https://github.com/can1357/oh-my-pi/blob/main/docs/settings.md), [Mnemopi](https://github.com/can1357/oh-my-pi/blob/main/docs/mnemosyne-memory-backend.md).

## 1. WebTeam là gì?

**WebTeam** là tổ chức kỹ thuật multi-agent dành cho phát triển ứng dụng web hiện đại. Mục tiêu của nó không chỉ là sinh code mà là đảm nhiệm một chu trình chuyên nghiệp:

**Khám phá yêu cầu → Chọn kỹ thuật → Thiết kế sản phẩm → Xây dựng → Kiểm thử → Review → Bảo mật → Triển khai (khi được duyệt) → Bảo trì và cải tiến.**

WebTeam ưu tiên backend **Node.js + Fastify + TypeScript + Zod + Biome**, database **SQLite hoặc MongoDB**, frontend **Vite + TypeScript + React hoặc SolidJS + TanStack + Zod + Biome**. Các dependencies bổ sung phải có lý do kỹ thuật; không cài hàng loạt vì “hiện đại”.

Hệ thống sử dụng tối đa **16 vai trò chuyên môn có sẵn**, nhưng thông thường mỗi tác vụ chỉ huy động một nhóm nhỏ. `webteam-orchestrator` nhận yêu cầu, chọn chuyên gia, cấp phạm vi, điều phối review và trả kết quả. Chủ dự án vẫn giữ quyền quyết định đối với lựa chọn quan trọng.

## 2. Hai cấp: Global WebTeam và Project WebTeam

| Cấp | Chức năng | Phạm vi |
|---|---|---|
| **Global WebTeam** | 16 agents, chuyên môn chung, kỹ năng nâng cao, policies, quy tắc routing/model, quy trình bootstrap | Tái sử dụng trên nhiều repository |
| **Project WebTeam** | Yêu cầu sản phẩm, Design DNA, kiến trúc, model constraints, coding conventions, tests, ADR và roadmap | Chỉ cho ứng dụng đang phát triển |

Cấu trúc minh họa (OMP phải xác nhận đường dẫn thực tế):

```text
~/.omp/agent/
  agents/
    webteam-orchestrator.md
    webteam-product.md
    ... (16 agent files)
  skills/
    design-master-workflow/SKILL.md
    webteam-deliberation-routing/SKILL.md
    playwright-visual-regression/SKILL.md
    ...
  config.yml
  webteam/                    # chỉ các tệp chính sách/tài liệu hỗ trợ; không giả định scan agent đệ quy

my-project/
  .omp/
    AGENTS.md
    RULES.md                  # khi thật sự cần và được OMP hỗ trợ
    config.yml                # khi dự án cần override
  docs/
    PRODUCT.md
    DESIGN.md
    ARCHITECTURE.md
    TECH_STACK.md
    ROADMAP.md
    DECISIONS.md
    TESTING.md
    design/                   # Design DNA, tokens, components, visual baselines
    engineering/              # Engineering DNA, coding/API conventions
    references/               # phân tích repo tham khảo
    deliberations/            # biên bản phản biện quan trọng (đã được làm sạch dữ liệu)
  apps/                       # nếu chọn monorepo
  packages/                   # nếu thật sự cần
```

### Có lưu agents vào thư mục con được không?

Thông thường OMP phát hiện các định nghĩa `agents/*.md` **trực tiếp**, không mặc nhiên quét `agents/webteam/*.md`. Khi bootstrap, bạn sẽ được hỏi muốn dùng folder riêng hay thư mục tiêu chuẩn. Chỉ dùng folder riêng khi bản OMP đang cài chứng minh được discovery và spawn. Cấu hình ổn định nhất thường là file phẳng với prefix `webteam-` trong `agents/`. Một extension/package OMP hợp lệ có thể là giải pháp đóng gói riêng nhưng phải kiểm thử trước.

## 3. Danh sách 16 agents

| # | Agent | Chức năng chính | Lúc nên gọi |
|---|---|---|---|
| 01 | `webteam-orchestrator` | Điều phối, onboarding, planning, risk/effort, hội đồng đa model, escalation và quality gates | Mọi yêu cầu phát triển web ở cấp dự án |
| 02 | `webteam-product` | Requirement engineering, user journeys, phân quyền, acceptance criteria | Tính năng mới, nghiệp vụ, thay đổi phạm vi |
| 03 | `webteam-designer` | UI/UX 8 bước, design system, palette, font pairing, anti-AI-slop, visual QA | Thiết kế mới, thay đổi giao diện, kiểm tra Design DNA |
| 04 | `webteam-architect` | System boundaries, modular architecture, ADR, reliability, architectural trade-offs | Hạ tầng, quyết định kiến trúc, refactor nhiều module |
| 05 | `webteam-frontend` | React/SolidJS, Vite, TanStack, type-safe forms, a11y, design-to-code | Xây dựng UI, quản lý trạng thái, routing |
| 06 | `webteam-backend` | Fastify, Node.js, TypeScript, Zod, auth, API lifecycle, observability | Business logic, API, service và auth |
| 07 | `webteam-database` | SQLite/MongoDB, schema, indexes, transactions, migrations, backup/restore | Thay đổi dữ liệu, truy vấn, di chuyển schema |
| 08 | `webteam-security` | Threat modeling, authorization, tenant isolation, OWASP, supply chain | Các phần xử lý dữ liệu hoặc quyền truy cập nhạy cảm |
| 09 | `webteam-qa` | Vitest unit/component/API/integration, Playwright E2E và visual regression | Lập kế hoạch test, regression, xác minh release |
| 10 | `webteam-devops` | Reproducible env, CI/CD, containers, monitoring, rollback, runbooks | CI, hosting và vận hành |
| 11 | `webteam-performance` | Core Web Vitals, profiling, API/db latency, caching và budgets | Có hiệu năng không đạt hoặc yêu cầu tải cao |
| 12 | `webteam-accessibility` | WCAG 2.2 AA, keyboard, focus, screen reader, inclusive UX | UI tương tác, form, dialog, dashboard |
| 13 | `webteam-reviewer` | Independent diff review, correctness, contracts, architecture drift | Những thay đổi cần đánh giá độc lập |
| 14 | `webteam-researcher` | Tài liệu chính thức, provider/model capabilities, code repo reference, license | Cần kiểm tra công nghệ, model, API hoặc repo tham khảo |
| 15 | `webteam-documentation` | Docs-as-code, API docs, project memory, onboarding và runbooks | Cần tài liệu chuẩn, cập nhật tri thức |
| 16 | `webteam-integration` | OAuth, webhook, external APIs, retries, idempotency, provider connectivity | Tích hợp dịch vụ, AI API, email, thanh toán |

**Không có 16 model chạy cùng lúc.** Đây là 16 vai trò, mỗi vai trò có thể dùng chung hoặc khác model tùy cấu hình. Orchestrator chỉ mở nhiệm vụ cho những specialist cần thiết.

## 4. Các nhóm kỹ năng nổi bật

### 4.1 Product, Architecture và Engineering

Tự tạo tài liệu sản phẩm; phân tích yêu cầu; xây kiến trúc; thiết kế contracts và ADR; giữ kiến trúc/flow phù hợp với source thực; quản lý migrations, security và các tiêu chuẩn code có thể kiểm tra.

### 4.2 Designer — workflow 8 giai đoạn

1. Product Context & Discovery.
2. Research & Reference Analysis.
3. Art Direction & Visual Identity.
4. Palette & Typography Engineering.
5. UX Architecture & Interaction Planning.
6. Design System & Component Specifications.
7. Design-to-Code Collaboration & Motion.
8. Visual QA, Anti-AI-Slop & Refinement.

Thiết kế được ghi vào `docs/DESIGN.md`, các design tokens và component contracts; GUI thực tế chỉ được xác nhận bằng kiểm tra browser/screenshot khi công cụ khả dụng.

### 4.3 QA và Playwright

WebTeam QA thực hiện kiểm thử phù hợp rủi ro:

- **Unit:** Vitest, fixtures, fake timers, mocks có kiểm soát, các nhánh nghiệp vụ.
- **Components:** React/SolidJS Testing Library, states, form validation, accessibility.
- **API:** Fastify `inject()`, Zod, authn/authz, contracts, negative cases.
- **Integration:** service ↔ database ↔ API, migrations, data isolation.
- **E2E:** Playwright, flows quan trọng, login, navigation, cross-browser nếu cần.
- **Visual:** `toHaveScreenshot()`, desktop/mobile, baseline có review, tránh false positive do font/OS/browser khác nhau.
- **Regression:** lặp lại lỗi thực, thêm bài test ngăn tái phát, CI gates theo mức rủi ro.

**Lưu ý:** Không tự động cập nhật visual baseline chỉ để làm test xanh; sự thay đổi giao diện phải được Designer/QA chấp nhận.

### 4.4 Học từ dự án hiện có và source bên ngoài

- `webteam-project-design-dna`: tìm phong cách giao diện thực tế, semantic colors, spacing, typography, component variants.
- `webteam-engineering-dna`: phát hiện conventions, module boundaries, API/test patterns.
- `webteam-design-preservation`: giữ các hợp đồng UI, behavior và visual snapshots.
- `webteam-reference-repository-intelligence`: xem repo GitHub/GitLab, pin commit, phân tích khả năng áp dụng, license và security.
- `webteam-standards-evolution`: đề xuất cải tiến có kiểm soát, có regression plan/ADR.

Mặc định phân tích repository ngoài ở chế độ **Learn Only**; không tự sao chép code hoặc thay đổi cấu trúc dự án.

## 5. Multi-Model Deliberation — nâng cấp từ R4, tiếp tục sử dụng trong R6

Đây là hệ thống **các model đưa ra phương án độc lập, phản biện bằng chứng và hỗ trợ quyết định quan trọng**. Nó không phải việc tự động hỏi nhiều model cho mọi câu lệnh.

### Ba chế độ

| Chế độ | Khi dùng | Hoạt động |
|---|---|---|
| **OFF** | Mặc định khi chưa bật hoặc công việc đơn giản | Agent chuyên môn + tests/review thông thường |
| **CHALLENGE** | Có rủi ro về tính đúng đắn hoặc quyết định kỹ thuật khó | Model A đề xuất, model B đánh giá độc lập và đưa phản ví dụ |
| **COUNCIL** | Vấn đề kiến trúc/authorization/migration cực kỳ quan trọng | 2–3 model/phương án; debate ngắn, test và Orchestrator phân xử |

Khi cài team lần đầu, bạn được hỏi:

- Bật hội đồng không? **OFF / ASK / AUTO theo quy tắc được duyệt**. Khuyến nghị **ASK**.
- Dùng model nào làm Primary, Proposer, Critic và Specialist; cùng provider hay nhiều provider?
- Loại công việc nào cần phản biện; tối đa bao nhiêu lần gọi/chi phí mỗi lần?
- Có được gửi code/tài liệu nội bộ tới từng provider không? Thông tin bí mật phải bị loại bỏ.
- Có bật Advisor/WATCHDOG liên tục không? Đây là tùy chọn **riêng**, không cần để dùng hội đồng.

OMP có thể hỗ trợ `modelRoles`, model selector trên từng item của `task`, custom agent definitions và `advisor`/`WATCHDOG` (cần kiểm tra bản đang cài). **Lưu ý quan trọng:** danh sách model trong một trường `model: [A, B]` là **thứ tự dự phòng**, không tạo hai model tranh luận. Hội đồng cần các task/model calls độc lập, thực sự sử dụng các model đã được phê duyệt. Advisor giám sát phiên chạy, **không đồng nghĩa** hội đồng quyết định.

### Trình tự hội đồng

```text
Rủi ro/độ khó đủ ngưỡng
  → Orchestrator chuẩn hóa câu hỏi, giới hạn code và ngân sách
  → Model A và Model B phân tích ĐỘC LẬP, chưa thấy ý kiến nhau
  → Trao đổi phản biện có giới hạn (thường 1 vòng)
  → QA/Security/Architect kiểm chứng qua code, tests, benchmark
  → Orchestrator lập quyết định dựa trên bằng chứng
  → Xin phê duyệt nếu có thay đổi quan trọng
  → Một implementation owner chỉnh sửa và chạy test
  → Lưu ADR/biên bản đã ẩn thông tin nhạy cảm
```

**Không chọn theo đa số phiếu**; test, security và yêu cầu sản phẩm được ưu tiên. Không cho các model cạnh tranh cùng ghi vào một cây thư mục. Nếu chỉ một model thực sự dùng được, hệ thống chuyển sang single-model review và **không được gọi đó là sự đồng thuận đa model**.

### Thêm model sau này

Orchestrator được phép **đề xuất**, không tự ý thêm model. Khi phát hiện thiếu năng lực (security, reasoning, vision, context, latency hoặc thiếu quan điểm độc lập), agent tạo `MODEL_ADDITION_PROPOSAL` gồm lý do, tùy chọn, giá/giới hạn đã xác minh, dữ liệu gửi sang provider, kế hoạch kiểm thử, rollback. Sau khi bạn duyệt, OMP mới được sửa cấu hình, kiểm tra credentials an toàn và thử gọi model trong giới hạn được phép.

## 5B. Primary provider, fallback khác provider và cấu hình tối ưu theo agent — R6

R6 phân biệt **ba chức năng độc lập**: Primary routing (mỗi agent chọn model phù hợp từ provider mặc định), **runtime fallback** (dự phòng nếu model/provider không sẵn sàng) và **multi-model deliberation** (nhiều model đánh giá độc lập). Việc bật tính năng này **không** bắt buộc sử dụng nhiều provider. Không bật fallback khi chưa xác nhận.

### 5B.1 Thứ tự hỏi khi cài đặt lần đầu

1. **Hỏi provider mặc định trước.** Orchestrator chỉ hiển thị tên những provider đã biết từ OMP, chẳng hạn DeepSeek, OpenAI hoặc local/custom provider; không tự mặc định DeepSeek. Alias `deepseek-flash` chỉ là ứng viên nếu provider tương ứng được bạn chọn và OMP xác nhận alias hoạt động.
2. **Sau khi chọn provider mặc định, kiểm tra danh sách model của chính provider đó.** Ghi lại thông tin model thực sự khám phá được: tên selector, authorization, reasoning/effort, context, tools, khả năng xử lý hình ảnh, giới hạn output, giá và mức sẵn sàng. Với danh sách lớn, Orchestrator lưu snapshot đầy đủ nhưng chỉ trình bày shortlist phù hợp cho bạn chọn.
3. **Hỏi fallback độc lập:** OFF — không đổi provider; ASK — hỏi trước từng lần chuyển khác provider (**khuyến nghị ban đầu**); AUTO — tự chuyển trong giới hạn provider/model/dữ liệu/chi phí đã duyệt.
4. **Chỉ nếu bật fallback:** hỏi bạn chọn một hoặc nhiều provider dự phòng, thứ tự ưu tiên, rồi mới khám phá các model của những provider đã chọn. Không tự mở tất cả provider có mặt trong hệ thống.
5. **Hỏi quyền chia sẻ mã nguồn và chi phí riêng cho từng provider.** Ví dụ có thể cho phép gửi code công khai nhưng không cho gửi code nội bộ hoặc log chứa dữ liệu cá nhân sang provider fallback.
6. **Sau đó mới hỏi multi-model deliberation, Caveman, Codebase Memory MCP, bố trí agents và các lựa chọn còn lại** theo Master Prompt. Một lần bật fallback không có nghĩa bạn đã đồng ý gọi hai model để tranh luận.
7. Xác nhận bảng routing và cấu hình dự kiến; sao lưu rồi mới áp dụng. Không thử request có phí khi chưa được phép.

### 5B.2 Các kỹ năng mới khi bootstrap

Master Prompt R6 yêu cầu tạo thêm những skills thực tế (tệp `SKILL.md`) để cài đặt/quản trị routing: `webteam-primary-provider-onboarding`, `webteam-model-capability-profiling`, `webteam-agent-model-optimizer`, `webteam-cross-provider-fallback`, `webteam-effective-routing-audit`, `webteam-model-compatibility-smoke-tests`, `webteam-provider-routing-evolution`. Orchestrator chỉ nạp các skills này trong lúc cài đặt, kiểm tra lỗi model hoặc thay đổi chính sách — không nạp cho mọi tác vụ code.

### 5B.3 Chọn fallback theo agent, không theo một danh sách đồng loạt

WebTeam tạo **16 Agent Model Profiles**. Mỗi profile ghi `primary_provider/model`, `fallback_provider/model` theo thứ tự, `thinking-level`, giới hạn context/compaction, yêu cầu tool calling, quyền truy cập Caveman/CBM, hành vi khi lỗi, mức riêng tư và bằng chứng xác minh. Orchestrator/Architect/Security có thể cần model lý luận tốt; Researcher/Documentation có thể ưu tiên chi phí và tốc độ; Designer/Accessibility có thể cần model nhìn ảnh nếu nhiệm vụ đòi screenshot; Frontend/Backend/QA cần model sử dụng tools ổn định.

**Các tool không được “cài cho từng model”:** Caveman và CBM chạy trong OMP/agent. Hệ thống xác minh model được chọn có thể sử dụng đúng tool API, sau đó chỉ cấp những công cụ phù hợp với role và nhiệm vụ. CBM không được tự động index lại toàn bộ repository mỗi khi fallback xảy ra.

### 5B.4 Cấu hình native minh họa

OMP hiện có `retry.modelFallback`, `retry.fallbackChains`, `retry.fallbackRevertPolicy`, `modelRoles` và danh sách model có thứ tự cho subagents. **Các selector bên dưới là placeholder, KHÔNG phải model thật:**

```yaml
# Chỉ minh họa trong OMP config.yml; dùng selector thật sau khi xác minh.
modelRoles:
  webteam_primary: "PRIMARY_PROVIDER/PRIMARY_MODEL"
  webteam_review: "PRIMARY_PROVIDER/REVIEW_MODEL:medium"
retry:
  modelFallback: true
  fallbackRevertPolicy: cooldown-expiry
  fallbackChains:
    webteam_primary:
      - "FALLBACK_PROVIDER/FALLBACK_MODEL:medium"
    webteam_review: []
```

Không sử dụng khóa không tồn tại như `retry.fallbackChains.agent:webteam-qa`. Per-agent fallback phải sử dụng selector có thứ tự trong agent hoặc các override mà phiên OMP của bạn thực sự hỗ trợ. **Danh sách model trong một subagent chưa chắc chặn được toàn bộ fallback từ cấu hình khác**; cần kiểm tra chain hiệu lực, đặc biệt các wildcard `provider/*` và chain `default` có thể được kế thừa.

**OFF đúng nghĩa:** Nếu không cho phép fallback khác provider, WebTeam phải bảo đảm không có đường chuyển âm thầm từ WebTeam sang provider chưa được phép. Không được phá những fallback hiện có của ứng dụng/agent khác chỉ để đạt mục tiêu này; cân nhắc sử dụng OMP profile riêng hoặc chặn chuyển ở bước gọi task.

### 5B.5 Các tình huống khi chạy

| Tình huống | Cách xử lý đúng |
|---|---|
| Model chính trả 429/timeout/outage đủ điều kiện retry | Kiểm tra chain, dữ liệu và quyền chi phí; ASK thì hỏi, AUTO thì chỉ dùng lựa chọn đã duyệt |
| Không có fallback hợp lệ | Báo lỗi hoặc đề xuất bổ sung model; không tự dùng model khác |
| Fallback có context nhỏ hơn | Tạo context handoff tối giản nhưng đầy đủ; nếu không an toàn thì dừng |
| Fallback không hỗ trợ required tools / ảnh | Không tiếp tục bước cần tool/vision; yêu cầu model khác hoặc thay đổi phạm vi được duyệt |
| Đang chạy migration/side-effect | Không tự retry một hành động không idempotent; kiểm tra trạng thái trước khi tiếp tục |
| Model fallback vô tình trùng model trong council | Không tính là hai đánh giá độc lập; điều phối phải sửa panel hoặc báo không đủ model |
| Việc khó nhưng model vẫn hoạt động | Dùng tăng effort/đề xuất deliberation, **không** viện cớ “khó” để kích hoạt outage fallback |

### 5B.6 Xem và thay đổi model trong tương lai

Bạn có thể yêu cầu:

> Audit all WebTeam model routes. Show which primary and fallback models each of the 16 agents actually resolves to, supported efforts, effective context limits, tool compatibility, fallback privacy and the health status of Caveman/Codebase Memory MCP. Propose changes only; ask before modifying provider configuration.

Hoặc:

> Propose a new cross-provider fallback for Security and Architect only. Discover candidate models **after** I approve the alternate provider, compare verified capabilities and cost, and do not activate the route until I approve the final matrix.

Orchestrator phải đưa ra `MODEL_ROUTING_CHANGE_PROPOSAL`, so sánh trước/sau, kiểm tra 16 agent profiles, xin phép và lưu changelog. Không tự kích hoạt provider mới hoặc sử dụng inference trả phí.


## 6. Cài Global WebTeam bằng Master Prompt

### 6.1 Chuẩn bị

1. Cài OhMyPi và xác nhận lệnh `omp` hoạt động trong terminal.
2. Chuẩn bị tối thiểu một provider/model khả dụng trong OMP, hoặc chuẩn bị thông tin để xác thực an toàn khi installer hỏi. **Provider mặc định do bạn chọn**, không cố định DeepSeek; giữ nguyên alias `deepseek-flash` nếu chọn đúng provider và OMP xác nhận alias hoạt động.
3. Chuẩn bị quyền đọc/ghi thư mục cấu hình OMP cần thiết; có Git hoặc backup khi sửa files cũ.
4. Không đưa API keys vào prompt, Markdown hay source control. Hãy đăng nhập/cấu hình credentials qua cơ chế an toàn của OMP/provider.
5. Chỉ bật Caveman hoặc Codebase Memory khi hiểu tác động network, quyền chạy installer và privacy/index.

Kiểm tra lệnh theo phiên bản đang cài; một số lệnh thường dùng là:

```bash
omp --version
omp models
omp models find deepseek       # ví dụ chỉ để tìm; thay bằng provider/model cần tra
omp config list --json
omp config path
```

`omp config path` hoặc cú pháp khác có thể không được hỗ trợ trên mọi bản; nếu thất bại, OMP cần tra tài liệu `--help` của bản đang chạy thay vì giả định đường dẫn mặc định.

### 6.2 Mở OMP và đưa Master Prompt

Trong terminal, mở phiên OMP tại một thư mục làm việc an toàn, rồi đưa toàn bộ nội dung [`WEBTEAM_ENTERPRISE_OMP_MASTER_PROMPT_R9.md`](./WEBTEAM_ENTERPRISE_OMP_MASTER_PROMPT_R9.md) vào session với chỉ dẫn:

> Execute this WebTeam Enterprise R9 bootstrap prompt in my active OhMyPi environment. First inspect the installed runtime, ask the mandatory global installation questions, preserve existing configuration, and implement/verify real agents, skills and policies. Do not create a web application yet.

Nếu phiên OMP không thể đọc file Markdown trực tiếp, dán nội dung Master Prompt vào chat của OMP. Không giả định có một lệnh nhập file cố định trên mọi bản OMP.

### 6.3 Onboarding Global bắt buộc

Đây là các lựa chọn cần được hỏi trước khi thay đổi cấu hình:

| Câu hỏi | Lựa chọn/khuyến nghị |
|---|---|
| Vị trí agents | `agents/webteam/` chỉ khi discovery được chứng minh; **flat `webteam-*.md`** là mặc định an toàn |
| Caveman | Có/Không; chỉ cài sau khi được phép |
| Codebase Memory MCP | Có/Không; kiểm tra thực tế trước khi sử dụng |
| **Provider mặc định (hỏi ĐẦU TIÊN)** | Bạn chọn DeepSeek, OpenAI, custom/local...; chỉ sau đó mới liệt kê toàn bộ model của provider đã chọn |
| Model chính cho agents | Chọn từ catalog đã xác minh; `deepseek-flash` chỉ là ứng viên nếu alias và provider phù hợp |
| Cross-provider fallback | **OFF / ASK / AUTO**, hỏi riêng; ASK là khuyến nghị cho lần đầu |
| Provider/model dự phòng | Chỉ liệt kê model sau khi bạn chọn provider fallback, kiểm tra effort/context/tool/chi phí |
| Quyền dùng dữ liệu khi fallback | Phê duyệt theo provider và mức độ nhạy cảm; không gửi secrets |
| Multi-model panel | **ASK** là khuyến nghị; OFF/AUTO cũng hợp lệ |
| Provider/models cho panel | Chọn từ danh sách OMP thực sự khám phá được, không tự bịa model |
| Chia sẻ code & dữ liệu | Phê duyệt theo provider; không gửi secrets |
| Giới hạn chi phí | Số lượt/model calls, thời gian và ngân sách khi có cách đo thực tế |
| Advisor/WATCHDOG | **OFF** cho tới khi người dùng tự bật |
| Cài provider/plugin | Chỉ sau khi xác nhận phạm vi và side effects |

Nếu chọn nhiều model nhưng chỉ một model hoạt động, WebTeam có thể cài các skills/policies ở trạng thái chờ, không tuyên bố hội đồng sẵn sàng. Nếu chọn một tích hợp bên ngoài là bắt buộc mà smoke test không đạt, nó phải dừng bước phụ thuộc và hỏi bạn sửa hoặc cho phép bỏ qua.

### 6.4 Caveman & Codebase Memory

Nguồn gốc cần kiểm tra khi cài:

- **Caveman:** <https://github.com/JuliusBrussee/caveman>. Có thể có installer OMP native; **đọc bản cài đang phát hành và kiểm tra mã trước khi chạy**, không chạy tự động các scripts từ URL không tin cậy.
- **Codebase Memory MCP:** <https://github.com/DeusData/codebase-memory-mcp>. Dùng knowledge graph của codebase; kiểm tra scope index, stale index, OMP MCP visibility và loại trừ `.env`, secrets, dữ liệu riêng tư.

Orchestrator phải xác nhận không trùng plugin/crew hiện có, kiểm tra trong chính OMP session, ghi health status, rồi mới kích hoạt những policies phù hợp cho từng agent. Không cần chạy graph indexing lớn cho mọi thay đổi nhỏ.

### 6.5 Kết quả cần thấy sau bootstrap

- 16 agents có tên `webteam-*` và được OMP discovery.
- Mỗi chuyên môn có `SKILL.md` hợp lệ, tài liệu reference liên quan, không chỉ tên skill.
- Provider mặc định do bạn chọn; 16 agent model profiles resolve và có fallback phù hợp/được tắt rõ ràng; policy effort/context/tool phản ánh các model thực.
- Panel OFF/ASK/AUTO lưu dưới dạng chính sách WebTeam; role selectors hoạt động khi được cấu hình.
- Các plugin/MCP được chọn hoạt động hoặc được báo `blocked`/`unverified` minh bạch.
- Có báo cáo smoke tests với lệnh, kết quả, files đã tạo và vấn đề tồn tại.
- Không có project mới được tự tạo nếu chưa yêu cầu.

## 7. Khởi tạo dự án web mới

### 7.1 Lệnh yêu cầu mẫu

```text
I want to create a new web application using WebTeam.
Start the new-project onboarding process.
Help me choose React or SolidJS, SQLite or MongoDB,
repository structure, design language, provider/model policy,
security, testing, deployment, and CI.
After my decisions are confirmed, generate real PRODUCT.md,
DESIGN.md, ARCHITECTURE.md, TECH_STACK.md, TESTING.md and ROADMAP.md.
Do not fabricate requirements or make paid/destructive changes without approval.
```

### 7.2 Quy trình dự kiến

Orchestrator sẽ hỏi theo từng nhóm: sản phẩm/người dùng → repo/runtime → backend/database → frontend/design → áp dụng/thu hẹp provider chính, fallback & hội đồng (kế thừa hoặc thu hẹp từ global) → kiểm thử/deploy. Sau khi chốt, Product viết `PRODUCT.md`, Designer viết `DESIGN.md`, Architect viết `ARCHITECTURE.md`, QA viết `TESTING.md`, DevOps viết runbooks, Orchestrator tạo `ROADMAP.md`, kiểm tra chéo và bắt đầu thực hiện những phần được cho phép.

Không phải mọi trường đều bắt buộc phải trả lời từng câu; WebTeam phải đề xuất defaults chuyên nghiệp và chỉ yêu cầu quyết định còn thiếu làm thay đổi thiết kế/kiến trúc đáng kể.

### 7.3 Ví dụ ngắn

```text
Build a Vietnamese school-management web application.
Use Fastify, TypeScript, Zod, Biome, SQLite initially,
and React + Vite + TanStack. I prefer a calm, highly usable
enterprise design. Ask me about roles, teacher workflows,
and report permissions. Reuse global WebTeam and its skills.
Use the multi-model CHALLENGE mode only for permission design,
data migrations or unresolved architectural trade-offs,
within my approved model/provider policy.
```

## 8. Tiếp quản repository đang có

Đưa OMP vào repo đang phát triển và dùng yêu cầu:

```text
Use WebTeam to adopt this existing repository safely.
Do not scaffold a new application or redesign it.
Inspect the implemented architecture and design conventions.
Run Project Design DNA and Engineering DNA discovery.
Create or reconcile the project documentation with the actual code.
Preserve current behavior, existing tokens and component APIs.
Present significant improvements and ask before migrations.
```

Kết quả mong muốn: báo cáo những thứ đã **xác minh từ code**, tiêu chuẩn có chứng cứ, Design DNA, Engineering DNA, các điểm lệch và kế hoạch thay đổi có thể kiểm thử. Dự án cũ **không** mặc nhiên bị viết lại theo template mới.

## 9. Học hỏi từ GitHub hoặc source code tham chiếu

```text
Analyze this repository as an external reference:
https://github.com/OWNER/REPOSITORY
Mode: Learn Only.
Pin the revision, inspect architecture, UI/design system,
code quality, dependencies, license and security implications.
Compare it with my current project and suggest transferable ideas.
Do not execute downloaded scripts or copy code without approval.
```

Sau phân tích, bạn có thể chọn **Selective Adoption** (lấy các patterns phù hợp) hoặc **Guided Migration** (chuyển đổi có kế hoạch). WebTeam phải ghi nguồn, revision, license/constraints, compatibility report, tests và rollback; không sao chép thương hiệu/tài sản không được cấp phép.

## 10. Yêu cầu hội đồng model cho một quyết định cụ thể

```text
Use WebTeam's approved multi-model CHALLENGE/COUNCIL protocol
for the tenant authorization architecture in this repository.
Have at least two genuinely distinct approved model routes
produce independent proposals before revealing conclusions.
Ask a security specialist to produce counterexamples.
Evaluate with real contract and permission tests,
record dissent, and ask me to approve any consequential change.
Do not let competing models write to the same files.
```

Nếu chưa có model thứ hai, Orchestrator phải thông báo rõ model thiếu, đề xuất bổ sung và chờ bạn chấp thuận (hoặc dùng single-model mode được mô tả trung thực).

## 11. Chọn model, role và reasoning/context

Hãy đọc mục **5B** về thứ tự chọn primary provider và fallback trước khi thay đổi cấu hình. Ví dụ role dưới đây chỉ hướng dẫn **multi-model panel** và phải được phối hợp với retry policy native cho fallback.

OMP có thể cấu hình role aliases cho agents và override từng task, nhưng phải xác minh bản cài. Ví dụ sau là **minh họa**, không copy nguyên các placeholder vào cấu hình vận hành:

```yaml
# Ví dụ định hướng; chỉ ghi sau khi tìm ra exact provider/model selectors
modelRoles:
  webteam_primary: PROVIDER/PRIMARY_MODEL
  webteam_critic: PROVIDER/CRITIC_MODEL
  webteam_specialist: PROVIDER/OPTIONAL_THIRD_MODEL
# Không bật advisor nền trừ khi bạn yêu cầu
advisor:
  enabled: false
```

Một agent định nghĩa `model: "@webteam_primary"` có thể dùng alias nếu OMP phát hiện role tương ứng. Effort `low`, `medium`, `high`, `max` ở chính sách WebTeam **không nhất thiết** map 1:1 sang API provider. Khi native `task.enableEffort` bật, OMP có thể sử dụng hint `lo|med|hi`; cần thử request thật để biết model có hỗ trợ hay không.

**Context:** không khai báo một con số 128K/256K/1M tùy ý. Phải dùng giới hạn thật từ provider/model, cấp nội dung dựa trên nhiệm vụ, không tự động load cả repository hay toàn bộ skills. Codebase Memory (nếu có) giúp tìm phạm vi liên quan, không thay cho kiểm tra source/tests.

## 12. Chính sách bảo mật và quyền phê duyệt

Người dùng phê duyệt trước khi:

- Thay provider, dùng dịch vụ có phí hoặc vượt mức chi tiêu đã duyệt.
- Truyền code/dữ liệu nội bộ sang provider mới.
- Cài extension/MCP/installer có quyền hệ thống hay network đáng kể.
- Đổi database/kiến trúc quan trọng, chạy migration phá hủy dữ liệu.
- Xóa files quan trọng, tự deploy production, tự push/commit nếu chưa được cho phép.
- Thay toàn bộ hệ thống thiết kế/branding của dự án cũ.

Không đặt keys trong docs, logs, graph indexes hay prompts chuyển giữa models. Phân biệt **native tool permissions** với **quy tắc được mô tả bằng prompt**; không giả định prompt tạo ra sandbox hoặc hard cost cap.

## 13. Vòng đời tác vụ thường ngày

- Một lỗi CSS nhỏ: Frontend xử lý, kiểm thử phù hợp, không cần COUNCIL.
- Một API mới: Product/Backend, QA kiểm tra Zod + Fastify, Security nếu cần.
- Giao diện quan trọng: Designer 8 bước → Frontend → Accessibility/QA → screenshot review.
- Migration khó: Database/Architect/Security/QA và CHALLENGE/COUNCIL khi có rủi ro/độ không chắc đáng kể.
- Bug liên quan nhiều module: Orchestrator dùng Codebase Memory (nếu healthy) để định vị, xem code, chỉ giao một agent thực hiện sửa, chạy regression.

Mỗi kết quả cần nêu chính xác files thay đổi, commands/tests thực thi, pass/fail, nhận định còn chưa xác minh, quyết định cần phê duyệt và các bước tiếp theo.

## 14. Quản trị, cập nhật và gỡ bỏ

### 14.1 Cập nhật Global WebTeam

Dùng Master Prompt phiên bản mới và yêu cầu **upgrade-in-place**: phát hiện phiên bản hiện tại, sao lưu, diff, chỉ sửa files do WebTeam sở hữu, không ghi đè cấu hình người dùng. Kiểm tra agents/skills/model routes lại sau upgrade.

### 14.2 Thay đổi model hoặc giới hạn chi phí

Yêu cầu Orchestrator hiển thị model registry và proposal. Sau khi duyệt, OMP cập nhật mapping và kiểm tra resolution, effort, retry chains, quyền dữ liệu. Không bắt buộc toàn team chuyển model cùng lúc.

### 14.3 Tắt hội đồng/Advisor

Yêu cầu đặt `multi-model deliberation = OFF` trong chính sách WebTeam của dự án hoặc toàn cục. Nếu có bật native Advisor, tắt qua cơ chế hỗ trợ của OMP (ví dụ `/advisor off` trong phiên, hoặc chỉnh `advisor.enabled` sau khi xác minh). Hai việc là độc lập.

### 14.4 Gỡ WebTeam

Sao lưu trước; lập manifest những files do bootstrap đã tạo; chỉ gỡ agent/skill/metadata WebTeam và cấu hình do WebTeam sở hữu; tránh xóa bất kỳ `.omp/`, MCP, model setting hay project document chung khi không chắc ai đang dùng. Việc gỡ Caveman/Codebase Memory phải được yêu cầu riêng và kiểm tra những công cụ khác phụ thuộc vào chúng.

## 15. Troubleshooting

| Hiện tượng | Nguyên nhân cần kiểm tra | Hướng xử lý |
|---|---|---|
| Không tìm thấy `webteam-orchestrator` | Path/profile sai; đặt trong thư mục không quét; frontmatter không hợp lệ | Kiểm tra OMP active dir, discovery và spawn; chuyển về flat `agents/webteam-*.md` |
| Fallback tự nhảy sang provider chưa duyệt | Chuỗi `default` kế thừa, selector cụ thể, `provider/*` wildcard hoặc task override | Tạm tắt cross-provider fallback cho WebTeam, kiểm tra toàn bộ chain hiệu lực; cân nhắc profile riêng và xin phép trước khi sửa shared config |
| Fallback không gọi được Caveman/CBM | Model không hỗ trợ tool protocol, subagent thiếu tool hoặc MCP/index không sẵn sàng | Kiểm tra effective tool access, safe tool probe, không gán kỹ năng inherent cho model |
| Model alias không dùng được | Provider/model chưa registered/auth; role override; selector sai | Kiểm tra `omp models`, config effective và exact selector |
| Hai model “tranh luận” nhưng kết quả từ một model | Đã dùng list fallback `[A,B]` hoặc runtime tự fallback | Tạo hai task spawns độc lập, log resolved model, kiểm tra retry chains |
| Panel chạy quá tốn chi phí | Bật advisor mỗi turn hoặc panel không giới hạn | OFF/ASK, giảm participants/rounds, áp cost gate và phân loại task |
| Advisor review trùng Caveman/Reviewer | Nhiều review loops tự động cùng bật | Chỉ giữ một review owner, bật advisor tùy nhu cầu |
| Codebase Memory truy vấn thiếu | Index cũ, sai branch/scope, tool không visible | Kiểm tra index provenance/freshness; kiểm tra source trực tiếp |
| Playwright visual flaky | Font, browser build, OS, animation hoặc test data khác | Cố định env, ảnh baseline theo project; kiểm tra changes trước khi update |
| Designer tự thay style dự án cũ | Chưa load Design DNA / thiếu visual baseline | Khôi phục contract, hỏi phê duyệt thay đổi lớn, thêm visual regression |
| Cấu hình project ghi đè global | Settings precedence, arrays replace | Kiểm tra merged effective settings và backup/diff |
| Không thể cài plugin/provider | Thiếu quyền, plugin incompatibility hoặc auth | Ghi blocker, hỏi cho phép remediation hoặc fallback; không tuyên bố đã cài |

## 16. Giới hạn và tiêu chí xác minh

Tài liệu và prompt này **chưa thực thi cài đặt trong môi trường OMP của bạn**. Thành công thực tế chỉ được xác nhận khi phiên OMP của bạn đã tạo files và kiểm tra discovery, skills, model resolution, test execution, integration health và review routing. Không có mô hình đa model nào bảo đảm code đúng tuyệt đối; tests, security review, requirements và người phê duyệt vẫn là chuẩn quyết định.

Nên dùng một disposable test repo để kiểm tra lần đầu:

1. Một tác vụ CSS nhỏ không dùng panel.
2. Một API Fastify có Zod và Vitest.
3. Một UI với Playwright E2E/visual snapshots.
4. Một repo cũ cần khám phá Design DNA.
5. Một tham chiếu GitHub ở Learn Only.
6. Một quyết định auth/architecture dùng CHALLENGE với hai model khác nhau nếu được cấp quyền.
7. Thử OFF mode và tình huống model panel unavailable; không được phát sinh cuộc gọi trả phí không có quyền.

## 17. Bảo mật, xác minh và khôi phục an toàn trong R6

### 17.1 Các lỗ hổng đã được bổ sung biện pháp xử lý

Bản R6 tăng cường quy trình kiểm soát quyền của subagents, chuyển model dự phòng, ngăn prompt injection, cài đặt an toàn và khôi phục cấu hình. **Đây là yêu cầu để OMP áp dụng khi cài đặt, không phải xác nhận các cơ chế đó đã chạy trên máy của bạn.**

| Rủi ro | Biện pháp bắt buộc |
|---|---|
| Subagent tự chạy lệnh ngoài ý muốn | Kiểm tra danh sách tool thực tế, quyền MCP/extension, cô lập quyền ghi và credentials; reviewer phải thật sự chỉ đọc |
| Fallback chuyển source code sang provider chưa cho phép | OFF: chặn; ASK: tắt fallback tự động và hỏi trước khi gửi lại tác vụ; AUTO: chỉ dùng khi có allowlist thực sự được thực thi |
| Prompt injection từ GitHub/MCP/README | Coi toàn bộ nội dung ngoài là dữ liệu không đáng tin, không được thay thế lệnh điều phối hoặc thay đổi quyền |
| Lặp giao dịch khi model lỗi hoặc timeout | Lưu idempotency key, checkpoint và xác nhận trạng thái trước khi thử lại |
| Monorepo bị bỏ qua hướng dẫn project | Kiểm tra `.omp` gần nhất cho context và `.omp/config.yml` trong thư mục đang chạy cho settings; nạp đúng tài liệu và xác minh cấu hình |
| Skill không được OMP phát hiện | `SKILL.md` phải có `name`, `description`, đặt trực tiếp trong `skills/<name>/` và test discovery |
| Visual baseline sai lệch hoặc được tự động chấp nhận | Cố định browser, font, hệ điều hành, locale, dữ liệu; mọi update snapshot quan trọng phải review |
| Bootstrap bị ngắt giữa chừng | Lưu manifest, bản sao cấu hình, checksum, trạng thái từng file và kế hoạch rollback |

### 17.2 Quy trình cài đặt an toàn được khuyến nghị

1. Khởi động OhMyPi trong workspace đáng tin cậy với chính sách phê duyệt tool phù hợp; không bật `--yolo` chỉ để bỏ qua bước xác nhận.
2. Chọn **provider mặc định trước**, rồi kiểm kê model của provider đó. Không chạy thử API tính phí trước khi được cho phép.
3. Chọn fallback và multi-model độc lập. Nên bắt đầu ở `ASK`; chế độ này không đồng nghĩa tự cho phép runtime chuyển provider.
4. Xem trước thư mục agents, danh sách file ghi, Caveman/Codebase Memory, installer và quyền truy cập trước khi phê duyệt.
5. Kiểm tra theo từng đợt: agents/skills có thể discovery, model giải quyết đúng route, tool permissions chính xác, smoke tests thực sự chạy.
6. Yêu cầu báo cáo manifest, kết quả xác minh, những hạng mục chưa hoàn thành và phương án khôi phục.

### 17.3 Xử lý sự cố

**Fallback sai provider:** dừng thực thi, vô hiệu hóa fallback tự động của tác vụ hoặc sử dụng OMP profile cô lập; kiểm tra chain kế thừa, role, agent overrides và hooks. Không gửi dữ liệu sang provider khác nếu chưa được phê duyệt.

**Reviewer có quyền ghi/chạy lệnh:** thu hẹp quyền bằng cấu hình công cụ hoặc môi trường cô lập rồi kiểm tra lại. Một câu mô tả “read-only” trong prompt không đủ bảo vệ, nhất là với subagent chạy headless.

**Dự án con thiếu hướng dẫn:** kiểm tra `.omp` gần nhất cho project context, đồng thời kiểm tra `.omp/config.yml` tại cwd để biết settings hiệu lực; có thể chạy từ root hoặc tạo override hợp lệ, rồi xác minh cả hai.

**Cài đặt bị ngắt:** dựa trên manifest để tiếp tục từ các file đã được xác minh; không ghi đè thay đổi mới của người dùng và không gỡ công cụ không do WebTeam cài đặt.

**Visual test lỗi:** tìm nguyên nhân từ môi trường, font, browser và dữ liệu trước khi sửa snapshot; không tự động chấp nhận hàng loạt ảnh mới.

### 17.4 Giới hạn xác minh

Kiểm tra tài liệu Markdown không chứng minh tất cả tính năng đã chạy trong OMP thực tế. Cần kiểm thử trên máy cài đặt đối với quyền tool, version, model, fallback, MCP, visual tests và CI. Xem `WEBTEAM_R9_AUDIT_REPORT.md` để biết những gì đã sửa và các điểm còn phụ thuộc môi trường.

## 18. Tài liệu tham khảo

- [OMP main repository](https://github.com/can1357/oh-my-pi)
- [OMP task agent discovery](https://github.com/can1357/oh-my-pi/blob/main/docs/task-agent-discovery.md)
- [OMP task tool and per-item model selection](https://github.com/can1357/oh-my-pi/blob/main/docs/tools/task.md)
- [OMP model configuration](https://github.com/can1357/oh-my-pi/blob/main/docs/models.md)
- [OMP native retry, fallback chains and config precedence](https://github.com/can1357/oh-my-pi/blob/main/docs/settings.md)
- [OMP provider authentication and discovery](https://github.com/can1357/oh-my-pi/blob/main/docs/providers.md)
- [OMP Advisor / WATCHDOG](https://github.com/can1357/oh-my-pi/blob/main/docs/advisor-watchdog.md)
- [Caveman](https://github.com/JuliusBrussee/caveman)
- [Codebase Memory MCP](https://github.com/DeusData/codebase-memory-mcp)
- [Vitest](https://vitest.dev/guide/)
- [Playwright](https://playwright.dev/docs/writing-tests)
- [Playwright visual regression](https://playwright.dev/docs/test-snapshots)

---

**Khuyến nghị vận hành:** hỏi và chọn primary provider trước, giữ `deepseek-flash` chỉ nếu đúng lựa chọn và alias thực sự hợp lệ; bật cross-provider fallback ở chế độ ASK khi cần, chỉ dùng model đã xác minh; sử dụng single-model cho công việc hằng ngày; chọn **ASK** cho multi-model debate; chỉ gọi hai model khác nhau khi rủi ro/độ không chắc đủ lớn; dựa trên tests và bằng chứng để chọn phương án; đưa mọi thay đổi quan trọng cho chủ dự án phê duyệt.


---

## Cấu hình Mnemopi và nâng cấp trực tiếp từ R6

Sử dụng `WEBTEAM_ENTERPRISE_OMP_MASTER_PROMPT_R9.md` để **cài WebTeam mới** và `WEBTEAM_R6_TO_MNEMOPI_R9_UPGRADE_PROMPT.md` để **nâng cấp đội R6 đã cài**. Mnemopi là backend tích hợp sẵn trong OhMyPi, không phải Codebase Memory MCP. Cấu hình khuyến nghị: bộ nhớ riêng từng dự án, chỉ lưu bài học đã kiểm chứng bằng công cụ (`autoRetain: false`), local embeddings khi được cho phép, không gọi model phụ cho memory (`llmMode: none`) và Auto-Learn review-first (`autoContinue: false`, `minToolCalls: 8`). Việc nâng cấp R6 không được tạo lại 16 agents, xóa dữ liệu nhớ hoặc thay đổi model routing.

Kiểm tra với `/memory view`, `/memory stats`, `/memory diagnose`, thử nhớ qua phiên mới và cách ly dự án. `/memory clear` có thể xóa dữ liệu. Tham khảo [tài liệu Mnemopi](https://github.com/can1357/oh-my-pi/blob/main/docs/mnemosyne-memory-backend.md).


---

## R9 — Quản trị Memory Hybrid: Global và từng Project

WebTeam áp dụng **hai cấp chính sách tri thức**: Global WebTeam quy định cách học và kiểm duyệt, còn mỗi dự án mặc định có bộ nhớ Mnemopi riêng cùng các kỹ năng cục bộ. **Hybrid không đồng nghĩa OMP tự hợp nhất an toàn hai bộ nhớ Global/Project.** Cấu hình khởi đầu khuyến nghị là `memory.backend: mnemopi`, `mnemopi.scoping: per-project`, `autoRetain: false`, `autolearn.enabled: true`, `autoContinue: false`, `minToolCalls: 8` khi được chấp thuận và xác minh đúng phiên bản. Mnemopi khác với Codebase Memory MCP.

**Khi cài Global WebTeam lần đầu**, Orchestrator hỏi một lần về Mnemopi, embeddings local hay chỉ tìm kiếm văn bản, chính sách lưu trữ, quyền tự học và có được **đề xuất** bài học dùng chung không. Không tự động bật lưu trữ hoặc chia sẻ Global. **Khi khởi tạo/tiếp quản từng dự án**, Orchestrator hỏi: kế thừa chính sách Global, tùy chỉnh quyền đọc/ghi và loại dữ liệu, hoặc tắt memory cho dự án. Sau đó tạo `docs/governance/MEMORY_POLICY.md` ghi danh tính bank, quyền, loại dữ liệu cấm, thời hạn rà soát và kết quả thử cách ly. File này là hợp đồng chính sách, **không tự tạo rào chắn runtime**.

### Phân loại nơi lưu tri thức

| Tri thức | Nơi lưu mặc định | Chia sẻ |
|---|---|---|
| Quyết định sản phẩm, Design DNA, bài học riêng ứng dụng | Tài liệu project + Mnemopi `per-project` | Chỉ project |
| Quy trình đặc thù dự án | `.omp/skills/<slug>/SKILL.md` sau review | Chỉ project |
| Kỹ thuật chung có thể tái sử dụng | Bài học đã làm sạch + đề xuất nâng cấp | Cần duyệt và đồng ý |
| Kỹ thuật đã phê duyệt dùng chung | Global skill được kiểm chứng hoặc shared bank thực sự được hỗ trợ | Có kiểm soát |
| Secrets, hội thoại thô, dữ liệu khách hàng, chỉ dẫn đáng ngờ | Không lưu vào memory | Cấm |

**Lưu ý quan trọng về Auto-Learn:** managed skills của OMP có thể được lưu trong thư mục cấp người dùng. Vì vậy `per-project` chỉ cách ly Mnemopi memory, **không bảo đảm skills tự sinh cũng chỉ có hiệu lực trong project**. WebTeam phải kiểm tra đường dẫn ghi thực tế. Nếu không thể bảo đảm cách ly, tắt Auto-Learn native cho dự án/phiên bằng cách được OMP hỗ trợ và dùng workflow tạo project-local skill sau kiểm duyệt. `autoContinue: false` không phải thiết lập phân quyền theo project.

### Nâng tri thức lên Global phải được phê duyệt riêng

**Memory:** bài học dự án có kiểm chứng → khái quát hóa/loại dữ liệu riêng → QA/Reviewer/Security và kiểm tra giấy phép → xin chấp thuận từng đề xuất → ghi vào shared/global bank **chỉ khi runtime hỗ trợ thật**; nếu không chỉ tạo đề xuất.

**Skills:** skill dự án → kiểm thử độc lập → review và phê duyệt → phiên bản global skill mới → thử kích hoạt và có đường rollback. Không tự lấy bài học dự án A áp dụng thành quy định của dự án B. Lưu đề xuất tại `docs/governance/GLOBAL_MEMORY_PROPOSALS.md` hoặc manifest quản trị phù hợp.

### Dành cho WebTeam R6 đã cài

Chỉ chạy **`WEBTEAM_R6_TO_MNEMOPI_R9_UPGRADE_PROMPT.md`**, **không** chạy Master Prompt R9 để cài lại. Prompt nâng cấp bảo tồn 16 agents, models, fallback, hội đồng multi-model, Caveman, Codebase Memory MCP và memory hiện có; chỉ thêm phỏng vấn chính sách từng dự án, bốn skills mới và kiểm tra cách ly. Các kết quả `PASS/FAIL/BLOCKED/UNVERIFIED` phải dựa vào chạy thử thực tế trên OMP, không chỉ dựa vào file Markdown.


