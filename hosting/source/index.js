const Odoo = require('odoo-xmlrpc');

const odoo = new Odoo({
  url: 'http://localhost',
  port: 8015,
  db: 'felino',
  username: 'ninofelino12@gmail.com',
  password: 'felino',
});

odoo.connect(async (err) => {
  if (err) {
    return console.error(err);
  }

  // Panggil model res.partner
  const partners = await odoo.execute('res.partner', 'search_read', [], ['name', 'email']);

  // Cetak hasil
  console.log(partners);

  // Disconnect
  odoo.disconnect();
});