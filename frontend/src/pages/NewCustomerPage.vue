<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Novo Cliente</div>
    <q-form @submit.prevent="createCustomer">
      <q-input filled v-model="form.name" label="Nome" class="q-mb-md" />
      <q-input filled v-model="form.phone" label="Telefone" class="q-mb-md" />
      <q-input filled v-model="form.email" label="Email" type="email" class="q-mb-md" />
      <q-input filled v-model="form.address" label="Endereço" class="q-mb-md" />
      <div class="q-mt-md">
        <q-btn label="Criar Cliente" type="submit" color="primary" />
      </div>
    </q-form>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
const form = ref({
  name: '',
  phone: '',
  email: '',
  address: ''
})

async function createCustomer() {
  try {
    const response = await axios.post('http://localhost:8000/customers', form.value)
    console.log('Cliente criado:', response.data)
    // Após criar, redireciona para a página de listagem de clientes
    router.push('/customers')
  } catch (error) {
    console.error('Erro ao criar cliente:', error)
  }
}
</script>
