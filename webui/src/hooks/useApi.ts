type AnyAsyncFuntion<TData = any> = (...args: any[]) => Promise<TData>;

export function useApi<
  TError = any,
  TApi extends AnyAsyncFuntion = AnyAsyncFuntion,
  TData = Awaited<ReturnType<TApi>>
>(
  api: TApi,
  options?: {
    failRule?: (data: TData) => boolean;
    message?: {
      success?: string;
      fail?: string;
      error?: string;
    };
  }
) {
  const data = ref<TData>();
  const isLoading = ref(false);

  const fetchResult = createEventHook<TData>();
  const fetchError = createEventHook<TError>();
  const fetchFinally = createEventHook();
  const message = useMessage();

  function execute(...params: Parameters<TApi>) {
    isLoading.value = true;

    api(...params)
      .then((res: TData) => {
        data.value = res;
        fetchResult.trigger(res);

        if (options?.failRule && options.failRule(res)) {
          options.message?.fail && message.error(options.message.fail);
        } else {
          options?.message?.success && message.success(options.message.success);
        }
      })
      .catch((err: TError) => {
        fetchError.trigger(err);

        options?.message?.error && message.error(options.message.error);
      })
      .finally(() => {
        isLoading.value = false;
        fetchFinally.trigger('');
      });
  }

  return {
    data,
    isLoading,

    execute,
    onResult: fetchResult.on,
    onError: fetchError.on,
    onFinally: fetchFinally.on,
  };
}
