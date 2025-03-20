<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">
      Modelos da Marca ID: {{ manufacturerId }}
    </div>

    <!-- QSelect para escolher o modelo -->
    <q-select
      v-model="selectedModel"
      :options="modelOptions"
      option-label="modelName"
      option-value="modelId"
      emit-value
      filled
      label="Selecione um modelo"
      class="q-mb-md"
    />

    <!-- Botão para ver detalhes do modelo (opcional) -->
    <q-btn label="Ver detalhes do modelo" color="primary" @click="showModelDetails" class="q-mr-sm" />

    <!-- Botão para navegar para a página de Tipos -->
    <q-btn
      label="Ver Tipos"
      color="secondary"
      @click="goToTypes"
      :disable="!selectedModel"
    />

    <!-- Exibir detalhes do modelo selecionado -->
    <div v-if="selectedModelDetails" class="q-mt-md">
      <h6>Detalhes do Modelo:</h6>
      <pre>{{ selectedModelDetails }}</pre>
    </div>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()

// O manufacturerId vem dos parâmetros da rota (ex: /models/121)
const manufacturerId = ref(route.params.manufacturerId)

// Armazenar os modelos retornados
const models = ref([])

// Preparar as opções para o QSelect
const modelOptions = ref([])

// O modelo selecionado (usando modelId)
const selectedModel = ref(null)

// Para exibir detalhes do modelo selecionado (opcional)
const selectedModelDetails = ref(null)

onMounted(async () => {
  try {
    const response = await axios.get(`http://localhost:8000/tecdoc/models/${manufacturerId.value}`)
    console.log('Resposta da API (Modelos):', response.data)
    if (response.data && response.data.models) {
      models.value = response.data.models
      modelOptions.value = models.value.map(item => ({
        modelId: item.modelId,
        modelName: item.modelName || item.modelname || 'Sem nome'
      }))
    } else {
      models.value = []
      modelOptions.value = []
    }
  } catch (err) {
    console.error('Erro ao carregar modelos:', err)
  }
})

function showModelDetails() {
  const found = models.value.find(m => m.modelId === selectedModel.value)
  selectedModelDetails.value = found || 'Nenhum detalhe disponível.'
}

function goToTypes() {
  if (!selectedModel.value) return
  // Navega para /types/:manufacturerId/:modelId
  router.push(`/types/${manufacturerId.value}/${selectedModel.value}`)
}
</script>
