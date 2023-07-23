<template>
    <div class="mx-auto grid max-w-2xl grid-cols-1 items-center lg:max-w-7xl lg:grid-cols-2 lg:px-8">
        <div class="p-3 sm:p-6 lg:flex-auto">
            <h2 class="text-2xl font-bold leading-9 tracking-tight text-gray-900">Create your account.</h2>
            <p class="mt-2 text-base leading-7 text-gray-600">Do you have an account? <RouterLink :to="{ 'name': 'login' }"
                    class="text-white bg-gradient-to-br from-green-400 to-blue-600 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-green-200 dark:focus:ring-green-800 font-medium rounded-lg text-sm px-2 py-1 text-center">
                    Click
                    here</RouterLink> to login.</p>
        </div>

        <div class="lg:mt-0 lg:w-full lg:max-w-md lg:flex-shrink-0 p-5">
            <div
                class="rounded-2xl bg-gray-50 py-10 ring-1 ring-inset ring-gray-900/5 lg:flex lg:flex-col lg:justify-center lg:py-16">
                <div class="flex min-h-full flex-1 flex-col justify-center px-6 lg:px-8">

                    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
                        <form class="space-y-6" action="" method="POST" v-on:submit.prevent="submitForm">
                            <div>
                                <div class="flex items-center justify-between">
                                    <label for="full-name" class="block text-sm font-medium leading-6 text-gray-900">
                                        Full Name</label>
                                    <div class="text-sm">
                                        <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500"></a>
                                    </div>
                                </div>

                                <div class="mt-2">
                                    <input id="full-name" name="full-name" v-model="form.name" type="text"
                                        autocomplete="text" required=""
                                        class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                                </div>

                                <div class="mt-5 flex items-center justify-between">
                                    <label for="email" class="block text-sm font-medium leading-6 text-gray-900">
                                        Email address</label>
                                    <div class="text-sm">
                                        <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500"></a>
                                    </div>
                                </div>

                                <div class="mt-2">
                                    <input id="email" name="email" v-model="form.email" type="email" autocomplete="email"
                                        required=""
                                        class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                                </div>
                            </div>

                            <div>
                                <div class="flex items-center justify-between">
                                    <label for="password"
                                        class="block text-sm font-medium leading-6 text-gray-900">Password</label>
                                    <div class="text-sm">
                                        <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Forgot
                                            password?</a>
                                    </div>
                                </div>
                                <div class="mt-2">
                                    <input id="password" name="password" v-model="form.password1" type="password"
                                        autocomplete="current-password" required=""
                                        class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                                </div>

                                <div class="mt-5 flex items-center justify-between">
                                    <label for="repeat password"
                                        class="block text-sm font-medium leading-6 text-gray-900">Repeat password</label>
                                    <div class="text-sm">
                                        <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500"></a>
                                    </div>
                                </div>
                                <div class="mt-2">
                                    <input id="repeat-password" name="repeat_password" v-model="form.password2"
                                        type="password" autocomplete="current-password" required=""
                                        class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                                </div>
                            </div>

                            <template v-if="errors.length > 0">
                                <div class="bg-red-300 text-white rounded-lg p-6">
                                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                                </div>
                            </template>

                            <div>
                                <button type="submit"
                                    class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign
                                    in</button>
                            </div>
                        </form>

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import { useToastStore } from '@/stores/toast'

export default {
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: ''
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.name === '') {
                this.errors.push('Your name is missing')
            }

            if (this.form.password1 === '') {
                this.errors.push('Your password is missing')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('The password does not match')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'The user is registered. Please log in', 'bg-emerald-300')

                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        } else {
                            this.toastStore.showToast(5000, 'Something went wrong. Please try again', 'bg-red-300')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>