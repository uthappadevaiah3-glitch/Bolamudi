// Bolamudi — nav toggle, scroll reveal, enquiry form handler
document.querySelector('.nav-toggle')?.addEventListener('click', function () {
  const nav = document.querySelector('nav.main');
  nav.classList.toggle('open');
  this.setAttribute('aria-expanded', nav.classList.contains('open'));
});

const io = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
}), { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Enquiries are emailed via Web3Forms; success replaces the form in place per spec §5.14.
// Endpoint (form action) and error text (data-error) come from config.py via the form markup.
document.querySelectorAll('form.enquiry').forEach(f => f.addEventListener('submit', async e => {
  e.preventDefault();
  if (!f.reportValidity()) return;
  const btn = f.querySelector('button[type=submit]'), label = btn.textContent;
  btn.disabled = true; btn.textContent = 'Sending…';
  try {
    const r = await fetch(f.action, { method: 'POST', body: new FormData(f) });
    if (!(await r.json()).success) throw 0;
    f.style.display = 'none';
    const s = f.parentElement.querySelector('.form-success');
    s.style.display = 'block';
    s.querySelector('h3')?.focus?.();
  } catch {
    btn.disabled = false; btn.textContent = label;
    alert(f.dataset.error);
  }
}));
