<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Clientes</div>

    <!-- Botão para adicionar novo cliente -->
    <q-btn label="Novo Cliente" color="primary" @click="openDialog = true" class="q-mb-md" />

    <!-- Tabela de Clientes -->
    <q-table
      :rows="customers"
      :columns="columns"
      row-key="id"
      flat
      bordered
      separator="horizontal"
    >
      <template v-slot:body-cell-actions="props">
        <q-td :props="props">
          <q-btn flat icon="edit" @click="editCustomer(props.row)" />
          <q-btn flat icon="delete" color="negative" @click="deleteCustomer(props.row.id)" />
        </q-td>
      </template>
    </q-table>

    <!-- Diálogo para criação/edição de clientes -->
    <q-dialog v-model="openDialog">
      <q-card>
        <q-card-section>
          <div class="text-h6">{{ isEditing ? 'Editar Cliente' : 'Novo Cliente' }}</div>
        </q-card-section>
        <q-card-section>
          <q-input filled v-model="form.name" label="Nome" />
          <q-input filled v-model="form.phone" label="Telefone" />
          <q-input filled v-model="form.email" label="Email" type="email" />
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="Cancelar" color="primary" v-close-popup />
          <q-btn flat label="Salvar" color="primary" @click="saveCustomer" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const customers = ref([])

const columns = [
  { name: 'id', label: 'ID', field: 'id', align: 'left', sortable: true },
  { name: 'name', label: 'Nome', field: 'name', align: 'left', sortable: true },
  { name: 'phone', label: 'Telefone', field: 'phone', align: 'left', sortable: true },
  { name: 'email', label: 'Email', field: 'email', align: 'left', sortable: true },
  { name: 'actions', label: 'Ações', align: 'center' }
]

const openDialog = ref(false)
const isEditing = ref(false)
const form = ref({
  id: null,
  name: '',
  phone: '',
  email: ''
})

// Busca todos os clientes
async function fetchCustomers() {
  try {
    const response = await axios.get('http://localhost:8000/customers')
    customers.value = response.data
  } catch (error) {
    console.error('Erro ao carregar clientes:', error)
  }
}

// Salva (cria ou atualiza) um cliente
async function saveCustomer() {
  try {
    if (isEditing.value) {
      // Atualizar cliente existente
      const response = await axios.put(`http://localhost:8000/customers/${form.value.id}`, form.value)
      const index = customers.value.findIndex(c => c.id === form.value.id)
      if (index !== -1) customers.value[index] = response.data
    } else {
      // Criar novo cliente
      const response = await axios.post('http://localhost:8000/customers', form.value)
      customers.value.push(response.data)
    }
    openDialog.value = false
    resetForm()
  } catch (error) {
    console.error('Erro ao salvar cliente:', error)
  }
}

// Prepara o formulário para edição
function editCustomer(customer) {
  isEditing.value = true
  form.value = { ...customer }
  openDialog.value = true
}

// Exclui um cliente
async function deleteCustomer(customerId) {
  try {
    await axios.delete(`http://localhost:8000/customers/${customerId}`)
    customers.value = customers.value.filter(c => c.id !== customerId)
  } catch (error) {
    console.error('Erro ao deletar cliente:', error)
  }
}

// Reseta os valores do formulário
function resetForm() {
  form.value = { id: null, name: '', phone: '', email: '' }
  isEditing.value = false
}

onMounted(() => {
  fetchCustomers()
})
</script>
