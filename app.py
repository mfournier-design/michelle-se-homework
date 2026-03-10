import requests
from flask import Flask, jsonify, request
import ldclient
from ldclient.config import Config
from ldclient.context import Context

LD_SDK_KEY = "REPLACE_WITH_YOUR_SDK_KEY"
LD_PROJECT_KEY = "ld-core-demo-mfournier"
LD_ENV_KEY = "test"
FLAG_KEY = "new-landing-component"

app = Flask(__name__)

ldclient.set_config(Config(LD_SDK_KEY))
ld = ldclient.get()

REMEDIATED = False

@app.route("/")
def home():
    return """
    <h1>LaunchDarkly SE Demo</h1>
<div style="display:flex; gap:12px; align-items:center; margin: 12px 0;">
  <button style="padding:10px 14px; font-size:16px;"
    onclick="(async () => { await fetch('/remediate', {method:'POST'}); await loadFlag(); })()">
    🚨 Remediate (Force OFF)
  </button>

  <button style="padding:10px 14px; font-size:16px;"
    onclick="(async () => { await fetch('/unremediate', {method:'POST'}); await loadFlag(); })()">
    ✅ Clear Remediation
  </button>
</div>
    <p><b>Flag value:</b> <span id="flag">loading...</span></p>
    <p><b>Remediation:</b> <span id="rem">loading...</span></p>
    <hr/>

    <div style="display:flex; gap:16px; align-items:center; flex-wrap:wrap;">
      <label>User key:
        <input id="key" value="demo-user" />
      </label>

      <label>Plan:
        <select id="plan">
          <option value="free">free</option>
          <option value="pro">pro</option>
        </select>
      </label>

      <label>Region:
        <select id="region">
          <option value="us">us</option>
          <option value="eu">eu</option>
        </select>
      </label>
    </div>

    <hr/>

    <!-- These ALWAYS exist on the page -->
    <div id="newComponent" style="display:none; border:2px solid green; padding:12px; margin:12px 0;">
      ✅ NEW LANDING COMPONENT (flag ON)
    </div>

    <div id="oldComponent" style="display:block; border:2px solid gray; padding:12px; margin:12px 0;">
      ⬅️ OLD LANDING (flag OFF)
    </div>

    <script>
      async function loadFlag() {
        try {
          const key = document.getElementById('key').value;
          const plan = document.getElementById('plan').value;
          const region = document.getElementById('region').value;

          const res = await fetch(`/evaluate?key=${encodeURIComponent(key)}&plan=${plan}&region=${region}`);
          const data = await res.json();

          document.getElementById('flag').innerText = data.value;
          document.getElementById('rem').innerText = data.remediated;
          document.getElementById('newComponent').style.display = data.value ? 'block' : 'none';
          document.getElementById('oldComponent').style.display = data.value ? 'none' : 'block';
        } catch (e) {
          document.getElementById('flag').innerText = "error (check terminal)";
        }
      }

      document.getElementById('key').addEventListener('input', loadFlag);
      document.getElementById('plan').addEventListener('change', loadFlag);
      document.getElementById('region').addEventListener('change', loadFlag);
      setInterval(loadFlag, 2000);
      loadFlag();
    </script>
    """

@app.route("/evaluate")
def evaluate():
    key = request.args.get("key", "demo-user")
    plan = request.args.get("plan", "free")
    region = request.args.get("region", "us")

    context = (
        Context.builder(key)
        .set("plan", plan)
        .set("region", region)
        .build()
    )

    value = ld.variation(FLAG_KEY, context, False)

    if REMEDIATED:
        value = False

    return jsonify({
        "flag_key": FLAG_KEY,
        "context_key": key,
        "plan": plan,
        "region": region,
        "value": value,
        "remediated": REMEDIATED
    })

@app.route("/remediate", methods=["POST"])
def remediate():
    global REMEDIATED
    REMEDIATED = True
    return jsonify({"ok": True, "remediated": True})

@app.route("/unremediate", methods=["POST"])
def unremediate():
    global REMEDIATED
    REMEDIATED = False
    return jsonify({"ok": True, "remediated": False})
  
if __name__ == "__main__":
    app.run(port=5001)