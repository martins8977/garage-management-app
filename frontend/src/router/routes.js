const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', redirect: '/login' },
      { path: 'login', component: () => import('pages/LoginPage.vue') },
      { path: 'customers', component: () => import('pages/CustomersPage.vue') },
      { path: 'customers/new', component: () => import('pages/NewCustomerPage.vue') },
      { path: 'brands', component: () => import('pages/BrandsPage.vue') },
      { path: 'models/:manufacturerId', component: () => import('pages/ModelsPage.vue') },
      { path: 'types/:manufacturerId/:modelId', component: () => import('pages/TypesPage.vue') },
      { path: 'categories/:manufacturerId', component: () => import('pages/CategoriesPage.vue') },
      { path: 'subcategories/:manufacturerId/:vehicleId', component: () => import('pages/SubCategoriesPage.vue') },
      { path: 'articles/:manufacturerId/:vehicleId/:subCategoryId', component: () => import('pages/ArticlesPage.vue') },
      { path: 'customers/:customerId/vehicles', component: () => import('pages/CustomerVehiclesPage.vue') },
      // (Opcional) Rota para criação de um novo veículo:
      { path: 'customers/:customerId/vehicles/new', component: () => import('pages/NewVehiclePage.vue') }
    ]
  },
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
