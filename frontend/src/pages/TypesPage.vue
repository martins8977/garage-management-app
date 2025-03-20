<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">
      Tipos para o Modelo ID: {{ modelId }} da Marca: {{ manufacturerId }}
    </div>

    <!-- Se houver engine types -->
    <div v-if="engineTypes.length">
      <!-- Itera sobre cada engine type retornado -->
      <div
        v-for="engine in engineTypes"
        :key="engine.vehicleId"
        class="q-mb-md row items-center"
        style="border: 1px solid #ccc; padding: 8px; border-radius: 4px;"
      >
        <!-- Coluna para exibir os campos do engine type -->
        <div class="col">
          <div><strong>Vehicle ID:</strong> {{ engine.vehicleId }}</div>
          <div><strong>Manufacturer:</strong> {{ engine.manufacturerName }}</div>
          <div><strong>Model Name:</strong> {{ engine.modelName }}</div>
          <div><strong>Type Engine:</strong> {{ engine.typeEngineName }}</div>
          <div>
            <strong>Construção:</strong>
            {{ engine.constructionIntervalStart }} - {{ engine.constructionIntervalEnd }}
          </div>
          <div><strong>Power (kW):</strong> {{ engine.powerKw }}</div>
          <div><strong>Power (PS):</strong> {{ engine.powerPs }}</div>
          <div><strong>Fuel Type:</strong> {{ engine.fuelType }}</div>
          <div><strong>Engine Codes:</strong> {{ engine.engineCodes }}</div>
          <!-- Adicione outros campos que deseja exibir -->
        </div>

        <!-- Coluna para o botão "Ver Peças" -->
        <div class="col-auto">
          <q-btn
            label="Ver Peças"
            color="primary"
            @click="goToSubcategories(engine.vehicleId)"
          />
        </div>
      </div>
    </div>

    <!-- Se não houver engine types -->
    <q-banner v-else class="q-mt-md" dense>
      Nenhum tipo encontrado.
    </q-banner>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()

const manufacturerId = ref(Number(route.params.manufacturerId))
const modelId = ref(Number(route.params.modelId))
const engineTypes = ref([])

// Função para buscar os tipos de motor (engine types) para este modelId e manufacturerId
async function fetchEngineTypes() {
  try {
    console.log('manufacturerId:', manufacturerId.value, 'modelId:', modelId.value)
    const response = await axios.get(
      `http://localhost:8000/tecdoc/engine-types/${manufacturerId.value}/${modelId.value}`
    )
    console.log('Resposta dos Tipos:', response.data)

    // Supondo que a resposta tem a chave "modelTypes" que é um array
    if (response.data && response.data.modelTypes) {
      engineTypes.value = response.data.modelTypes
    } else {
      engineTypes.value = []
    }
  } catch (error) {
    console.error("Erro ao carregar os tipos:", error)
  }
}

// Função chamada ao clicar no botão "Ver Peças"
function goToSubcategories(vehicleId) {
  // Navega para /subcategories/:manufacturerId/:vehicleId
  // onde será exibida a lista de categorias para este veículo
  router.push(`/subcategories/${manufacturerId.value}/${vehicleId}`)
}

onMounted(() => {
  fetchEngineTypes()
})
</script>
