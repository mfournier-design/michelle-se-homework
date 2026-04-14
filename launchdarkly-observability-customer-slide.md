# LaunchDarkly Observability
## One platform for signals, diagnosis, and safe releases

**Customer-facing slide copy (modeled for an executive layout)**

---

### Core in-app observability (Observe / Monitor)
- **Session Replay:** Replay user sessions before, during, and after incidents.
- **Errors, Logs, Traces, Metrics:** Unified telemetry to isolate issues quickly.
- **Dashboards + Alerts:** Custom health views and proactive threshold/query alerts.
- **Service Map + Unified Search Spec:** Cross-service visibility and consistent querying.
- **LLM Observability:** Prompt/response, latency, token usage, and provider metadata in traces.
- **Observability Settings:** Retention, privacy, and sampling controls at project level.

### SDK instrumentation + OpenTelemetry
- **Observability plugins (server-side + client-side):** Error monitoring, logging, tracing.
- **Session Replay plugin (client-side):** User journey visibility tied to telemetry.
- **Direct SDK emission:** Errors, logs, metrics, traces from LD SDK paths.
- **OTLP ingestion support:** Server-side OTEL collector + filters into LaunchDarkly Observability.
- **OpenLLMetry instrumentation:** LLM span capture in standard trace workflows.

### Data ingestion & ecosystem integrations
- **Native/connector inputs:** AWS CloudWatch Metrics (via Kinesis Firehose), AWS FireLens, Azure Monitor, Datadog Agent, Fluent Bit, Syslog log drain, Vercel.
- **Correlated analysis:** Third-party telemetry + LaunchDarkly SDK signals in one investigative workflow.

### Vega AI layer (Observability intelligence)
- **Vega Agent (AI debugger):** Summarizes logs/traces/errors/sessions, identifies likely root causes, and correlates with recent flag/code changes.
- **Vega Search Assistant:** Natural-language investigation across observability datasets.
- **Context-aware entry points:** Works from individual log lines, traces, errors, sessions, alerts, and query views.
- **Emerging auto-remediation vision:** AI-guided remediation and rollback recommendations tied to releases.

### UI + release-level capabilities
- **Session Replay + Heatmaps:** Faster bug reproduction and UX friction analysis.
- **In-app feedback (flag-aware):** Feedback tied to feature flags and linked sessions.
- **Guarded releases integration:** Use errors/metrics/traces as rollout guardrails for rollback/self-healing patterns.
- **Release health analytics:** Operational visibility for engineering and leadership.

---

## Suggested on-slide layout (single slide)

**Title bar:**  
**LaunchDarkly Observability: From telemetry to safer releases**

**Subtitle:**  
Unify product, platform, and AI signals to diagnose faster and ship with confidence.

**Body (2x3 grid):**
1. Core In-App Observability
2. SDK + OTEL Instrumentation
3. Ingestion & Integrations
4. Vega AI Intelligence
5. UI + Release Guardrails
6. Business Outcomes

**Business Outcomes tile (concise):**
- Reduce MTTR with end-to-end correlation
- Catch regressions earlier in rollouts
- Improve release confidence with automated guardrails
- Scale observability for traditional + LLM-powered applications

**Footer CTA:**  
**Next step:** Message **AJ Garron 🤝** for a one-on-one via Reclaim.ai.

---

## Presenter notes (optional)
- Lead with unified workflow: detect (alerts), diagnose (logs/traces/errors/sessions), decide (Vega + guardrails), act (rollback/remediation patterns).
- Highlight differentiation: **flag-aware observability** connects release events and code changes to runtime impact.
- For AI/LLM workloads, emphasize OpenLLMetry + LLM span detail as part of the same trace-centric operating model.
