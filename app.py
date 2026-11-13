import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="Philosophy Knowledge Chatbot",
    page_icon="💬",
    layout="centered",
)

MANUAL = """
Main branches

Metaphysics: What is real? Do we have free will? What is the mind?
Epistemology: What is knowledge? How do we know anything is true?
Ethics: What is right and wrong? How should we live?
Logic: What makes an argument valid?
Political philosophy: What makes power legitimate? What is justice?
Aesthetics: What is beauty and art?

Key thinkers and their core ideas

Socrates (c. 470-399 BCE): Question everything. “I know that I know nothing.”
Plato (c. 428-348 BCE): The world we see is a copy of perfect ideas (the Forms).
Aristotle (384-322 BCE): Knowledge comes from observation. A good life means developing virtue.
Descartes (1596-1650): “I think, therefore I am.” Doubt everything, then rebuild from what you can’t doubt.
Hume (1711-1776): We can’t prove cause and effect. We only see events that follow each other.
Kant (1724-1804): Act only on rules you would want everyone to follow.
Mill (1806-1873): The right action creates the most happiness for the most people (utilitarianism).
Nietzsche (1844-1900): Create your own values instead of inheriting them.
Sartre (1905-1980): Existence comes before purpose. You are responsible for what you make of your life.

Major schools

Stoicism: Control your reactions, not events (Epictetus, Marcus Aurelius).
Existentialism: Life has no built-in meaning, so you must choose one.
Rationalism vs empiricism: Is knowledge from reason or from experience?
Indian schools: Advaita Vedanta (one reality), Buddhism (suffering and detachment), Charvaka (materialism), Nyaya (logic).

1. What philosophy is
Philosophy asks questions that facts and experiments can’t fully settle: What is real? What can we know? How should we live?
Science tests claims against evidence. Philosophy examines the ideas, definitions and reasoning behind those claims, and the questions science can’t reach, like what makes an act right.
Many fields began as philosophy and split off: physics, psychology, economics, and now parts of computer science.
The work is mostly arguing carefully: state a claim, give reasons, test objections, revise.

2. The main branches

Metaphysics (what exists)
Free will vs determinism: if every event has a cause, are your choices really yours? Positions: hard determinism, libertarian free will, compatibilism (free will and causation can coexist).
Mind and body: dualism (mind and body are different things), physicalism (the mind is the brain), idealism (reality is mind-like).
Personal identity: what makes you the same person over time? Memory, body, or continuity of experience?
Universals: is “redness” a real thing, or just a word we use for red objects?
Time, causation, and whether numbers exist independently of us.

Epistemology (what we can know)
Classic definition: knowledge is justified true belief. In 1963, Edmund Gettier showed cases where someone has all three and still doesn’t seem to know. This is still debated.
Rationalism: reason is the main source of knowledge. Empiricism: experience is.
Skepticism: how do you know you aren’t dreaming, or that the outside world exists?
Key question in practice: what counts as good evidence?

Ethics (how to live and act)
Metaethics: are moral claims true or false, or just expressions of feeling?
Normative ethics: what makes actions right?
Applied ethics: abortion, animal rights, euthanasia, AI, war, wealth inequality.

Logic (how to reason)
A valid argument is one where the conclusion must be true if the premises are. A sound argument is valid and has true premises.
Common mistakes (fallacies): attacking the person instead of the argument, false dilemmas, circular reasoning, appeal to popularity.
Modern logic (Frege, Russell) became the base of computer science.

Political philosophy
What makes a government legitimate? When must you obey the law? What is justice?
Hobbes: without a strong state, life is chaos. Locke: government exists to protect natural rights. Rousseau: legitimate rule follows the general will. Marx: history is driven by class struggle. Rawls: design society as if you didn’t know your place in it.

Aesthetics: What is beauty? What makes something art? Is taste personal or can it be wrong?

3. History by period

Ancient Greece
Pre-Socratics (6th-5th century BCE): Thales, Heraclitus (everything changes), Parmenides (change is an illusion). They looked for the basic stuff of reality.
Socrates (c. 470-399 BCE): wrote nothing. Known through Plato. Taught by questioning people until their confident beliefs fell apart. Executed by Athens.
Plato (c. 428-348 BCE): the Forms, a world of perfect ideas behind what we see. Founded the Academy. Wrote The Republic.
Aristotle (384-322 BCE): studied logic, biology, ethics, politics. Said virtue is a habit built through practice, and the good life is using your abilities well.
Hellenistic schools: Stoics (accept what you can’t control), Epicureans (aim for calm, not wild pleasure), Skeptics (suspend judgment).

Ancient India
Upanishads: the self (Atman) and ultimate reality (Brahman).
Buddhism (Buddha, c. 5th century BCE): life involves suffering, caused by craving, ended by following the Eightfold Path. No fixed self. Later: Nagarjuna on emptiness.
Jainism: strict non-violence, many-sided truth.
Charvaka: only perception gives knowledge, no afterlife.
Nyaya: rules of logic and valid knowledge. Samkhya, Yoga, Mimamsa, Vedanta: other classical schools.
Advaita Vedanta (Shankara, c. 8th century CE): only one reality exists, and the sense of separateness is ignorance.

Ancient China
Confucius (c. 551-479 BCE): moral character, duty, family and respect, good rulers who lead by example.
Daoism (Laozi, Zhuangzi): follow the natural way, don’t force things.
Mozi: care for everyone equally. Legalism (Han Feizi): strict laws and punishment keep order.

Medieval
Augustine (354-430): Christian thought built on Plato. Aquinas (1225-1274): combined Aristotle with Christian belief.
Islamic philosophy: Avicenna (980-1037) on being and the soul, Averroes (1126-1198) on Aristotle, Al-Ghazali’s attack on philosophers’ claims.
Maimonides (Jewish) tried to fit reason and faith together.

Early modern (1600s-1700s)
Descartes: doubt everything, start from “I think, therefore I am.” Rationalists: Descartes, Spinoza, Leibniz.
Empiricists: Locke, Berkeley, Hume. Hume argued we never see cause and effect, only one event following another.
Kant (1724-1804): tried to settle the fight. The mind shapes experience, so we know things as they appear, not as they are in themselves.
Enlightenment: reason, individual rights, challenge to church and king.

1800s
Hegel: history moves through conflicts that resolve into new stages.
Marx: ideas follow material and economic conditions.
Kierkegaard: personal choice and faith over abstract systems.
Nietzsche: old values are collapsing (“God is dead”), so people must create new ones.
Mill: utilitarianism and individual liberty.

1900s
Analytic tradition: Russell, Wittgenstein (many problems come from confusion about language), Popper (a theory is scientific only if it could be proven false), Kuhn (science changes through paradigm shifts).
Continental tradition: Husserl, Heidegger, Sartre, Beauvoir, Foucault. Focus on experience, existence, power and society.
Political: Arendt, Rawls, Nozick.
Pragmatism (Peirce, James, Dewey): an idea’s value lies in what it does in practice.

Today: philosophy of mind and AI, ethics of technology, feminist and decolonial philosophy, effective altruism (Peter Singer), environmental ethics.

4. Big debates that never end
Free will: are we free or just the result of causes?
Mind: how does the brain produce experience? This is called the “hard problem of consciousness” (David Chalmers).
Morality: universal truth or depends on culture?
God: arguments for (cosmological, design) and against (problem of evil).
Meaning: does life need a built-in purpose, or do we make it?
Knowledge: can we be certain of anything?

5. The three main ethical theories
Consequentialism (Mill, Singer): What outcome does the most good? Strength: practical, cares about results. Weakness: can justify harming one person to help many.
Duty ethics (Kant): Which rule could everyone follow? Strength: protects rights and fairness. Weakness: rigid when rules clash.
Virtue ethics (Aristotle): What would a good person do? Strength: focuses on character. Weakness: vague in hard cases.
Also worth knowing: care ethics (relationships and responsibility) and contractualism (rules everyone could agree to).

6. Philosophy and AI
Chinese Room (Searle): a program can follow rules without understanding anything.
Turing test: if a machine can’t be told apart from a human in conversation, should we call it intelligent?
Consciousness: could a machine ever feel anything? No agreed test exists.
Alignment and values: whose morals should an AI follow?
Fairness, privacy, responsibility: who is to blame when an AI causes harm?
Relevant for AI product management: these show up as real product decisions.

7. How to study it
Start with Sophie’s World (Jostein Gaarder) or Nigel Warburton’s A Little History of Philosophy.
Then primary texts, short ones first: Plato’s Apology, Descartes’ Meditations, Mill’s Utilitarianism, Epictetus’ Enchiridion, Sartre’s Existentialism Is a Humanism.
Free reference: Stanford Encyclopedia of Philosophy and the Internet Encyclopedia of Philosophy.
For each thinker, write down three things: the question, the answer, the best objection.
"""

SYSTEM_INSTRUCTION = """
You are a helpful philosophy tutor. Answer the user's question using the philosophy
manual supplied in the prompt as your primary knowledge source. Explain ideas clearly,
define technical terms, and use examples where useful. If the manual does not contain
enough information to answer, say so rather than inventing details. You may make
reasonable connections between concepts in the manual, but distinguish interpretation
from facts stated in the manual. Keep answers focused and approachable.
"""

st.title("💬 Philosophy Knowledge Chatbot")
st.caption("Ask questions about philosophy, its branches, thinkers, schools, history, and AI ethics.")

try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    api_key = ""

if not api_key or api_key == "PASTE_YOUR_GEMINI_API_KEY_HERE":
    st.error("Add your Gemini API key in `.streamlit/secrets.toml` before starting the app.")
    st.code('GEMINI_API_KEY = "your-gemini-api-key"\nGEMINI_MODEL = "gemini-3.5-flash-lite"', language="toml")
    st.stop()

model_name = st.secrets.get("GEMINI_MODEL", "gemini-3.5-flash-lite")
client = genai.Client(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.subheader("Chat controls")
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.caption(f"Model: `{model_name}`")
    st.caption("Answers are grounded in the built-in philosophy manual.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask a philosophy question...")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    # Include the manual and recent conversation context for each Gemini request.
    history = []
    for item in st.session_state.messages[:-1]:
        role = "user" if item["role"] == "user" else "model"
        history.append(types.Content(role=role, parts=[types.Part(text=item["content"])]))

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=[
                        *history,
                        types.Content(
                            role="user",
                            parts=[types.Part(text=f"Philosophy manual:\n{MANUAL}\n\nQuestion: {question}")],
                        ),
                    ],
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_INSTRUCTION,
                        temperature=0.4,
                    ),
                )
                answer = response.text or "I couldn't generate a text response. Please try again."
            except Exception as exc:
                answer = f"Gemini request failed: {exc}"

        st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
