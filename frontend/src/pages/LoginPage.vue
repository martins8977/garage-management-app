<template>
  <q-page class="flex flex-center">
    <q-card class="q-pa-lg" style="width: 300px">
      <q-card-section>
        <div class="text-h6">Login</div>
      </q-card-section>

      <q-card-section>
        <q-input v-model="username" label="Username" outlined dense />
        <q-input v-model="password" label="Password" type="password" outlined dense class="q-mt-md" />
      </q-card-section>

      <q-card-actions align="right">
        <q-btn label="Login" color="primary" @click="handleLogin" />
      </q-card-actions>

      <q-card-section v-if="errorMessage" class="text-negative text-caption">
        {{ errorMessage }}
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { login } from 'src/services/auth'

const username = ref('')
const password = ref('')
const errorMessage = ref('')
const router = useRouter()

const handleLogin = async () => {
  const success = await login(username.value, password.value)
  if (success) {
    router.push('/brands') // ou outro caminho que tiveres pós-login
  } else {
    errorMessage.value = 'Credenciais inválidas. Tenta novamente.'
  }
}
</script>
