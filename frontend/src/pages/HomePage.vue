<template>
  <q-page class="q-pa-md flex flex-center">
    <div class="text-center">
      <h1 class="q-mb-md">Bem-vindo ao Sistema de Gestão de Garagem</h1>
      <q-btn label="Listar Clientes" color="primary" class="q-mb-sm" @click="goToCustomers" />
      <q-btn label="Novo Cliente" color="secondary" @click="goToNewCustomer" />
    </div>
  </q-page>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

function goToCustomers() {
  router.push('/customers')
}

function goToNewCustomer() {
  router.push('/customers/new')
}
</script>
