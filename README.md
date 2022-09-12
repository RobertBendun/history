# Programmer's calendar

This project is an attempt to register major events in history of programming languages like:

- programming language celebrities birthday
- major releases of various programming languages
- key events that allowed the diversity of the programming world today

Feel free to contribute since it's mostly manual work. Data in all shape and sizes is welcome here ❤️.

## Programming languages format

Using typescript-like notation where:

- `T[]` means array with elements of type T
- `{ "foo": T; }` means object with key `foo` and of value with type `T`
- null and string describe respective JSON values

```typescript
{
	"name": string | string[];
	"website": string | null;
	"influenced_by": string[];
	"releases": {
		"version": string;
		"date": string;
		"features": string[];
	}[];
}
```
