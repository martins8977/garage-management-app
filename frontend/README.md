# Garage Manager (frontend)

Garage Manager

## Install the dependencies
```bash
yarn
# or
npm install
```

### Start the app in development mode (hot-code reloading, error reporting, etc.)
```bash
quasar dev
```


### Lint the files
```bash
yarn lint
# or
npm run lint
```


### Format the files
```bash
yarn format
# or
npm run format
```


### Build the app for production
```bash
quasar build
```

### Customize the configuration
See [Configuring quasar.config.js](https://v2.quasar.dev/quasar-cli-vite/quasar-config-js).


###########################################

Próximos Passos
Listar Modelos:
Poderás criar uma segunda página ou um seletor na mesma página para, ao clicar numa marca, chamar o endpoint GET /tecdoc/models/{manufacturer_id} e listar os modelos.

Navegação entre as páginas:
Se quiseres, podes criar um fluxo onde o utilizador seleciona uma marca na tabela e é redirecionado para outra página onde listam-se os modelos correspondentes.

Integração com o resto do core:

Vehicles: armazenar manufacturerId no registo do veículo do cliente.
Inventário / Peças: utilizar a TecDoc para buscar categorias e artigos (peças) relacionadas ao veículo.