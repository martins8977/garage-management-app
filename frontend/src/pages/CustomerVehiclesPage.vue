<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">
      Veículos do Cliente: {{ customerId }}
    </div>

    <q-table
      title="Lista de Veículos"
      :data="vehicles"
      :columns="columns"
      row-key="id"
      flat
      bordered
    />

    <div class="q-mt-md">
      <q-btn label="Novo Veículo" color="primary" @click="goToNewVehicle" />
    </div>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()

// O customerId é recebido dos parâmetros da rota
const customerId = ref(route.params.customerId)

// Variável para armazenar os veículos deste cliente
const vehicles = ref([])

// Definição das colunas para a QTable (ajuste conforme os campos do veículo)
const columns = [
  { name: 'id', label: 'ID', field: 'id', align: 'left' },
  { name: 'license_plate', label: 'Matrícula', field: 'license_plate', align: 'left' },
  { name: 'brand', label: 'Marca', field: 'brand', align: 'left' },
  { name: 'model', label: 'Modelo', field: 'model', align: 'left' },
  { name: 'year', label: 'Ano', field: 'year', align: 'center' }
]

// Função para buscar os veículos do cliente no backend
async function fetchVehicles() {
  try {
    // Ajuste o endpoint conforme sua implementação no backend
    const response = await axios.get(`http://localhost:8000/customers/${customerId.value}/vehicles`)
    vehicles.value = response.data
  } catch (error) {
    console.error("Erro ao carregar os veículos:", error)
  }
}

// Navegar para a página de criação de um novo veículo
function goToNewVehicle() {
  router.push(`/customers/${customerId.value}/vehicles/new`)
}

// Ao montar, buscar os veículos
onMounted(() => {
  fetchVehicles()
})
</script>

<style scoped>
/* Adicione estilos conforme necessário */
</style>
